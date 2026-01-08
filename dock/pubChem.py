import csv
import subprocess

import requests
from pathlib import Path
import shutil
import time

# =========================
# 路径配置
# =========================
CHEMBL_FILE = Path("CHEMBL.txt")
CID_FILE = Path("CID.txt")
RESULT_FILE = Path("chembl_intid_mapping.csv")

SRC_PDB_DIR = Path(r"D:\dock\HTMDv3\HTMDv3_vina\PubChem_ligand\ligand_pdb")
DST_COPY_PDB_DIR = Path(r"D:\dock\ligand_pdb\copy_ligand_pdb")
DST_DOWNLOAD_SDF_DIR = Path(r"D:\dock\ligand_pdb\download_ligand_sdf")
DST_DOWNLOAD_SDF_CONVERT_PDB_DIR = Path(r"D:\dock\ligand_pdb\download_ligand_sdf_convert_pdb")

# =========================
# HTTP 配置
# =========================
BASE_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/disambiguate/name/JSON"
TIMEOUT = 10
REQUEST_INTERVAL = 30  # 防止请求过快被限流


# =========================
# 核心逻辑
# =========================
def fetch_intid(name: str) -> str | None:
    """
    根据 name 请求 PubChem API，返回 IntID（CID）
    """
    time.sleep(REQUEST_INTERVAL)
    try:
        resp = requests.get(
            BASE_URL,
            params={"name": name},
            timeout=TIMEOUT
        )
        if resp.status_code != 200:
            return None

        data = resp.json()
        records = data.get("Disambiguation", {}).get("Record", [])

        for record in records:
            if record.get("IDType") == "CID" and "IntID" in record:
                return str(record["IntID"])

        return None
    except Exception:
        return None


def copy_pdb_by_intid(intid: str, exist_skip=True):
    """
    在源目录中查找包含 IntID 的 pdb 文件并复制
    """

    pdb_file_name = f"{intid}.pdb"

    # 构建文件路径
    file_path = DST_COPY_PDB_DIR / pdb_file_name

    # 检查文件是否已存在
    if exist_skip and file_path.exists():
        print(f"文件已存在: {file_path}，跳过复制")
        return True

    shutil.copy2(SRC_PDB_DIR / pdb_file_name, file_path)


def is_contain_pdb(intid: str):
    """
    在源目录中查找包含 IntID 的 pdb 文件
    """
    for pdb_file in SRC_PDB_DIR.glob("*.pdb"):
        if str(intid) == pdb_file.name.replace(".pdb", ""):
            return True
    return False


def load_cache(cache_file: Path) -> dict[str, str | None]:
    """
    读取 chembl_intid_mapping.csv
    返回: {name: IntID or None}
    """
    cache = {}
    if not cache_file.exists():
        return cache

    with cache_file.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"].strip()
            intid = row["IntID"].strip()
            cache[name] = intid if intid else None

    return cache


def download_sdf(cid, record_type, exist_skip=True):
    """下载单个化合物的3D/2D SDF文件"""

    # 构建文件路径
    file_path = DST_DOWNLOAD_SDF_DIR / f"{cid}.{record_type}.sdf"

    # 检查文件是否已存在
    if exist_skip and file_path.exists():
        print(f"文件已存在: {file_path}，跳过下载")
        return True

    time.sleep(REQUEST_INTERVAL)
    try:
        # 使用PUG-REST API获取3D构象
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/record/SDF?record_type={record_type}"
        response = requests.get(url)

        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
            return True
        else:
            print(f"下载CID {cid} {record_type} 失败，状态码: {response.status_code}")
        return False
    except Exception as e:
        print(f"处理CID {cid} {record_type} 时出错: {str(e)}")
    return False


OBABEL_BIN = "obabel"  # 如不在 PATH 中，写绝对路径


def convert_sdf_2_pdb(sdf_file_dir: Path, pdb_file_dir: Path):
    pdb_file_dir.mkdir(parents=True, exist_ok=True)

    for sdf_file in sdf_file_dir.glob("*.sdf"):
        # 只对 3d 结构或没有表明 2d 或 3d 的 sdf 转换为 pdb
        if ".3d" in sdf_file.stem or (".2d" not in sdf_file.stem and ".3d" not in sdf_file.stem):
            pdb_file_name = f"{sdf_file.stem}.pdb".replace(".3d", "").replace(".2d", "")
            pdb_file = pdb_file_dir / pdb_file_name

            if pdb_file.exists():
                print(f"[SKIP] {pdb_file.name}")
                continue

            cmd = [
                OBABEL_BIN,
                str(sdf_file),
                "-O",
                str(pdb_file),
                "-h"
            ]

            print(" ".join(cmd))

            try:
                result = subprocess.run(
                    cmd,
                    shell=True,
                    check=True
                )

                print(f"[OK] {sdf_file.name} -> {pdb_file.name}")
            except subprocess.CalledProcessError as e:
                print(f"[FAIL] {sdf_file.name}")
                print(e.stderr)


def main():
    if not CHEMBL_FILE.exists():
        raise FileNotFoundError(f"{CHEMBL_FILE} 不存在")

    DST_COPY_PDB_DIR.mkdir(parents=True, exist_ok=True)
    DST_DOWNLOAD_SDF_DIR.mkdir(parents=True, exist_ok=True)

    cache = load_cache(RESULT_FILE)

    results = []

    with CHEMBL_FILE.open("r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]

    download_failed_files = []
    for idx, name in enumerate(names, 1):
        if name in cache:
            intid = cache[name]
        else:
            intid = fetch_intid(name)

        intid = intid if intid is not None else ""
        print(f"[{idx}/{len(names)}] 处理 {name} CID 结果 {intid}")

        results.append((name, intid))

        if intid:
            if is_contain_pdb(intid):
                # 首先从已有 pdb 文件列表中复制
                copy_pdb_by_intid(intid)
            else:
                # 其次从 pubChem 网站中下载
                res_3d = download_sdf(intid, "3d")
                if not res_3d:
                    res_2d = download_sdf(intid, "2d")
                    if not res_2d:
                        download_failed_files.append(intid)

    # 保存 name ↔ IntID 映射结果
    with RESULT_FILE.open("w", encoding="utf-8") as f:
        f.write("name,IntID\n")
        for name, intid in results:
            f.write(f"{name},{intid}\n")

    print("处理完成")
    print(f"映射结果已保存至: {RESULT_FILE}")
    print(f"pubChem 下载失败的 CID：{download_failed_files}")


def main2():
    if not CID_FILE.exists():
        raise FileNotFoundError(f"[FAIL] {CID_FILE} 不存在")

    DST_COPY_PDB_DIR.mkdir(parents=True, exist_ok=True)
    DST_DOWNLOAD_SDF_DIR.mkdir(parents=True, exist_ok=True)

    with CID_FILE.open("r", encoding="utf-8") as f:
        cids = [line.strip() for line in f if line.strip()]

    download_failed_files = []
    for idx, cid in enumerate(cids, 1):
        print(f"[{idx}/{len(cids)}] 处理 CID {cid}")

        if is_contain_pdb(cid):
            # 首先从已有 pdb 文件列表中复制
            copy_pdb_by_intid(cid)
        else:
            # 其次从 pubChem 网站中下载
            res_3d = download_sdf(cid, "3d")
            if not res_3d:
                res_2d = download_sdf(cid, "2d")
                if not res_2d:
                    download_failed_files.append(cid)

    print("处理完成")
    print(f"pubChem 下载失败的 CID：{download_failed_files}")


if __name__ == "__main__":
    # main()
    # main2()
    convert_sdf_2_pdb(DST_DOWNLOAD_SDF_DIR, DST_DOWNLOAD_SDF_CONVERT_PDB_DIR)