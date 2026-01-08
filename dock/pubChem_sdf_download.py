import os
import requests
from concurrent.futures import ThreadPoolExecutor

# 创建保存目录
output_dir = "pubchem_sdf_files"
os.makedirs(output_dir, exist_ok=True)


# 单个CID的SDF下载函数
def download_sdf(cid):
    """下载单个化合物的3D SDF文件"""
    try:
        # 使用PUG-REST API获取3D构象
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/record/SDF?record_type=3d"
        response = requests.get(url)

        if response.status_code == 200:
            with open(f"{output_dir}/{cid}.sdf", "wb") as f:
                f.write(response.content)
            return True
        else:
            print(f"下载CID {cid}失败，状态码: {response.status_code}")
        return False
    except Exception as e:
        print(f"处理CID {cid}时出错: {str(e)}")
    return False


# 批量下载，使用多线程加速
def batch_download_sdf(cid_list, max_workers=10):
    """批量下载多个化合物的SDF文件"""
    success_count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(download_sdf, cid_list))
        success_count = sum(results)

    print(f"共下载成功{success_count}/{len(cid_list)}个SDF文件")
    return success_count


# 执行批量下载（限制数量，避免过载PubChem服务器）
download_sdf(2795)
