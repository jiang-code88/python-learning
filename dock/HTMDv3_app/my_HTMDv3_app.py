#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, time
import subprocess
import pandas as pd
import shutil
import re, openpyxl
import openbabel
import threading
import xlsxwriter  # 调用模块
import streamlit as st
import py3Dmol
import streamlit.components.v1 as components

# Streamlit界面
# 美化页面并添加图片
st.set_page_config(page_title="蛋白质配体对接分析", page_icon="🔬", layout="wide")
# 自定义CSS样式来添加背景图片
background_image_url = \
    "https://img.pptjia.com/image/20181121/fc28da12ef7e66124969445bb6a3eda2.png"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 页面标题
st.title("蛋白质配体对接分析")

# 设置参数
st.sidebar.header("设置参数")
work_dir = st.sidebar.text_input("工作目录路径，注意：要求全英文！", r"D:\dock\TEXT")
protein_name = st.sidebar.text_input("请输入你的目标蛋白名称", "protein")
run_button1 = st.sidebar.button("可视化蛋白质")
pdb_file = st.sidebar.file_uploader("上传处理后的蛋白质PDB文件", type="pdb")
chain_ids = st.sidebar.text_input("目标链，例如：A 或者 A;B", "A")  # 输入你需要分析的目标链
check = st.sidebar.text_input("选择结合口袋设置策略：blindness或者amino acid", "blindness")
amino_acid_ID = st.sidebar.text_input("如果选择amino acid，请输入氨基酸序号", "NA")
CPU_core = st.sidebar.text_input("输入用于计算内核（系统核数/3）", "32")
thread = st.sidebar.text_input("输入需要使用的线程数量", "1")
mgltools_path = st.sidebar.text_input("MGLTools安装目录", r"C:\Program Files (x86)\MGLTools-1.5.7")
run_button2 = st.sidebar.button("运行分析")
work_dir = work_dir.replace("\\", "/")

###############################
protein_dir = os.path.join(work_dir, protein_name)
vina_result_dir = os.path.join(protein_dir, 'vina_result')
ligand_pdbqt_dir = os.path.join(work_dir, "ligand_pdbqt")
###############################


st.write(
    "高通量分子对接技术是一种重要的计算机辅助药物设计方法，"
    "通过模拟小分子配体与目标蛋白质受体之间的结合过程，筛选和优化潜在的药物候选分子。"
    "该技术结合了计算化学、分子建模和生物信息学等多学科方法，"
    "能够高效地预测小分子与蛋白质的相互作用模式和结合能，"
    "评估小分子的活性和选择性，从而加速药物发现过程。")


def remove_water_and_ligands(pdb_file, output_file):
    with open(pdb_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # 保留ATOM和HETATM行，排除水分子（HOH）、配体和离子
            if line.startswith("ATOM"):
                res_name = line[17:20].strip()  # 获取残基名称（20列-23列）
                # 排除水分子（HOH）、配体和离子（根据实际情况调整）
                if res_name == "HOH" or res_name in ["LIG", "ION", "UNK"]:
                    continue
                # 如果是蛋白质的原子，则写入输出文件
                outfile.write(line)


# 定义支持的函数和类
def compute_center_of_mass(pdb_file):
    x_coords = []
    y_coords = []
    z_coords = []

    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith("ATOM"):  # 过滤ATOM或HETATM行
                # 解析出坐标值
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                x_coords.append(x)
                y_coords.append(y)
                z_coords.append(z)

    # 计算质心
    center_x = sum(x_coords) / len(x_coords) if x_coords else 0
    center_y = sum(y_coords) / len(y_coords) if y_coords else 0
    center_z = sum(z_coords) / len(z_coords) if z_coords else 0

    return center_x, center_y, center_z


def compute_bounding_box(pdb_file):
    x_coords = []
    y_coords = []
    z_coords = []

    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith("ATOM"):  # 过滤ATOM或HETATM行
                # 解析出坐标值
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                x_coords.append(x)
                y_coords.append(y)
                z_coords.append(z)

    # 计算包围盒的大小
    if x_coords and y_coords and z_coords:
        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)
        min_z, max_z = min(z_coords), max(z_coords)
        size_x = max_x - min_x
        size_y = max_y - min_y
        size_z = max_z - min_z
        return size_x, size_y, size_z
    else:
        return 0, 0, 0  # 如果没有坐标数据，返回 (0, 0, 0)


def get_residue_coordinates(pdb_file, chain_id, residue_number):
    with open(pdb_file, 'r') as file:
        for line in file:
            if line.startswith("ATOM"):
                # 获取链ID、残基编号和原子名称
                chain = line[21:22].strip()
                res_num = int(line[22:26].strip())
                atom_name = line[12:16].strip()

                # 检查是否是目标残基的alpha碳（CA）
                if chain == chain_id and res_num == residue_number and atom_name == "CA":
                    # 获取alpha碳原子的坐标
                    x = float(line[30:38].strip())
                    y = float(line[38:46].strip())
                    z = float(line[46:54].strip())
                    return x, y, z

    raise ValueError(f"Residue {residue_number} in chain {chain_id} not found.")


def get_file_names_without_extension(folder_path):
    file_names = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            name_without_extension = os.path.splitext(file_name)[0]
            file_names.append(name_without_extension)
    return file_names


# 共享变量来存储每个线程的进度
progress_values = [0, 0, 0]


def run_qvina(s, n_list, start, end, thread_id, CPU):
    for x in range(start, end):
        # 更新进度
        progress = (x - start + 1) / (end - start)
        progress_values[thread_id - 1] = progress
        os.chdir(os.path.join(work_dir, protein_filename, "analzy", s[x]))
        command = ('vina --config ' + str(s[x]) + '_config.txt --log ' + str(s[x]) + '.txt --out ' +
                   str(s[x]) + '_out.pdbqt --exhaustiveness=' + CPU)
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if result.returncode == 0:
            print(f"线程【{thread_id}】执行成功！！！还剩【{end - (x + 1)}】个小分子！！！")
        else:
            print(f"线程【{thread_id}】{str(s[x])}命令执行失败，返回代码: {result.returncode}")

    print(f"线程【{thread_id}】运行完成！！！")


def model1():
    dest_dir = work_dir + "\\" + protein_filename + '\\vina_result'  ###vina_result路径
    for num in range(0, n_list):  # 按行对文件内容的读取；
        file_dir = work_dir + "\\" + protein_filename + '\\analzy\\' + s[num]  ####analyze文件夹工作路径
        file_name_list = os.listdir(file_dir)
        for file in file_name_list:
            if file == s[num] + ".txt":
                source_file = file_dir + '\\' + file  # 移动前文件
                shutil.move(source_file, dest_dir)


def model2():
    dest_dir = work_dir + "\\" + protein_filename + '\\vina_result'  ###vina_result路径
    for num in range(n_list, len(s)):  # 按行对文件内容的读取；
        file_dir = work_dir + "\\" + protein_filename + '\\analzy\\' + s[num]  ####analyze文件夹工作路径
        file_name_list = os.listdir(file_dir)
        for file in file_name_list:
            if file == s[num] + ".txt":
                source_file = file_dir + '\\' + file  # 移动前文件
                shutil.move(source_file, dest_dir)


def delete_files(files):
    for file in files:
        file_path = os.path.join(work_dir, file)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"[remove] 删除文件 {file}")
        else:
            print(f"[remove] 文件 {file} 不存在")


def extract_amino_acid_sequence_by_chain(pdb_file):
    chain_sequences = {}  # 用于存储每个链的氨基酸序列

    with open(pdb_file, 'r') as infile:
        prev_res_num = None  # 用来存储上一个残基的编号
        current_chain = None  # 当前链的标识符
        for line in infile:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                res_name = line[17:20].strip()  # 获取残基名称（20列-23列）
                res_num = int(line[22:26].strip())  # 获取残基编号（23列-26列）
                chain_id = line[21]  # 获取链标识符（22列）

                # 如果是新的链，初始化一个新列表
                if chain_id != current_chain:
                    current_chain = chain_id
                    chain_sequences[current_chain] = []

                # 确保每个残基编号只被记录一次
                if res_num != prev_res_num:
                    chain_sequences[current_chain].append((res_num, res_name))  # 存储编号和氨基酸名称
                    prev_res_num = res_num

    # 将氨基酸序列编号和名称按链分开输出
    formatted_sequences = {}
    for chain, amino_acids in chain_sequences.items():
        formatted_sequence = ' '.join([f"{res_num},{res_name}" for res_num, res_name in amino_acids])  # 按照要求的格式拼接
        formatted_sequence = formatted_sequence.replace(" ", "; ")  # 使用分号分隔每对编号和名称
        formatted_sequences[chain] = formatted_sequence

    # 展示每个链的氨基酸序列
    for chain, sequence in formatted_sequences.items():
        st.write(f"Chain {chain}: {sequence}")

    return formatted_sequences  # 返回按链划分的氨基酸序列


if run_button1 and protein_name is not None:
    ###预先展示蛋白质
    os.makedirs(work_dir, exist_ok=True)
    pdb_file_path = os.path.join(work_dir, protein_name + ".pdb")
    pdb_file = os.path.join(work_dir, protein_name + ".pdb")
    output_file = os.path.join(work_dir, protein_name + "_processed.pdb")  # 输出文件路径
    remove_water_and_ligands(pdb_file, output_file)
    time.sleep(3)
    protein_name_1 = protein_name + "_processed.pdb"
    pdb_file_path_3D = os.path.join(work_dir, protein_name_1)
    os.chdir(work_dir)
    st.write("-----可视化蛋白质结构-----")
    # 可视化蛋白质结构
    view = py3Dmol.view(width=800, height=600)
    view.addModel(open(pdb_file_path_3D, 'r').read(), 'pdb')
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.zoomTo()
    tmp_html = os.path.join(work_dir, "tmp.html")
    with open(tmp_html, 'w') as f:
        f.write(view._make_html())
    # 使用Streamlit组件展示HTML内容
    with open(tmp_html, 'r') as f:
        html_content = f.read()
        components.html(html_content, height=600)
    # 使用示例
    st.write(
        "-----目标蛋白质氨基酸序列展示如下，若使用特定氨基酸作为对接盒子中心，请将下方特定氨基酸序号填入左侧“amino_acid_ID”-----")
    pdb_file1 = protein_name_1  # 输入文件路径
    sequence = extract_amino_acid_sequence_by_chain(pdb_file1)
    st.write("-----结束目标受体蛋白质预处理，接下来开始对接之旅！！！-----")

if run_button2 and pdb_file is not None:
    thread = int(thread)
    st.write("-----开始生成目标受体蛋白质PDBQT-----")
    time.sleep(3)
    pdb_file_path = os.path.join(work_dir, protein_name + ".pdb")
    pdb_file = os.path.join(work_dir, protein_name + ".pdb")
    output_file = os.path.join(work_dir, protein_name + "_processed.pdb")  # 输出文件路径
    protein_name_1 = protein_name + "_processed.pdb"
    # 使用MGLTools生成PDBQT文件
    python_exe = os.path.join(mgltools_path, 'python.exe')
    prepare_receptor_script = os.path.join(mgltools_path,
                                           'Lib/site-packages/AutoDockTools/Utilities24/prepare_receptor4.py')
    command = f'"{python_exe}" "{prepare_receptor_script}" -r {protein_name_1} -A hydrogens -o processed_protein.pdbqt'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    process.wait()

    if process.returncode == 0:
        st.write("受体PDBQT文件生成成功")
    else:
        st.write(f"命令执行失败，返回代码: {process.returncode}")
    st.write("-----目标受体蛋白质PDBQT已生成-----")
    st.write("-----计算受体蛋白质中心位置，并设置对接盒子-----")
    time.sleep(3)
    receptor_pdbqt = 'processed_protein.pdbqt'
    if check == "blindness":

        center_x, center_y, center_z = compute_center_of_mass(receptor_pdbqt)
        size_x, size_y, size_z = compute_bounding_box(receptor_pdbqt)
        st.write("-----受体蛋白质中心位置：-----")
        st.write(f'Center of mass: x={center_x:.3f}, y={center_y:.3f}, z={center_z:.3f}')
        st.write("-----受体蛋白质对接盒子尺寸：-----")
        st.write(f'Bounding box size: x={size_x:.3f}, y={size_y:.3f}, z={size_z:.3f}')
    else:
        chain_id = chain_ids  # 替换为你的链ID
        residue_number = int(amino_acid_ID)  # 替换为你的氨基酸编号
        coords = get_residue_coordinates(receptor_pdbqt, chain_id, residue_number)
        center_x, center_y, center_z = coords
        size_x, size_y, size_z = 40, 40, 40  # 设置盒子大小，可以根据实际情况调整
        print(f'Center of mass: x={center_x:.3f}, y={center_y:.3f}, z={center_z:.3f}')
        st.write("-----受体蛋白质中心位置：-----")
        st.write(f'Center of mass: x={center_x:.3f}, y={center_y:.3f}, z={center_z:.3f}')
        st.write("-----受体蛋白质对接盒子尺寸：-----")
        st.write(f'Bounding box size: x={size_x:.3f}, y={size_y:.3f}, z={size_z:.3f}')

    # 创建必要的文件夹
    st.write("-----创建受体蛋白质文件夹，这是专属于它的工作目录-----")
    path_analzy = os.path.join(work_dir, "ligand_pdbqt")
    os.makedirs(path_analzy, exist_ok=True)
    path_analzy2 = os.path.join(work_dir, "target_folder")
    os.makedirs(path_analzy2, exist_ok=True)

    # 转换配体文件
    st.write("-----配体文件的预处理，可能需要一点时间......-----")
    # 配体文件的预处理
    ligand_pdb_dir = os.path.join(work_dir, "ligand_pdb")
    ligand_pdbqt_dir = os.path.join(work_dir, "ligand_pdbqt")
    os.makedirs(ligand_pdbqt_dir, exist_ok=True)

    # 生成批处理文件
    bat_file_path = os.path.join(work_dir, "convert_ligands.bat")
    with open(bat_file_path, 'w') as bat_file:
        for filename in os.listdir(ligand_pdb_dir):
            if filename.endswith(".pdb"):
                input_path = os.path.join(ligand_pdb_dir, filename)
                output_path = os.path.join(ligand_pdbqt_dir, os.path.splitext(filename)[0] + ".pdbqt")
                bat_file.write(f'obabel "{input_path}" -O "{output_path}"\n')

    # 运行批处理文件
    try:
        result = subprocess.run(bat_file_path, shell=True, check=True)
        st.write("-----配体文件的预处理完成，其实也挺快-----")
    except subprocess.CalledProcessError as e:
        st.write(f"批处理文件执行失败，返回代码: {e.returncode}")

    time.sleep(5)
    folder_path = ligand_pdbqt_dir
    s = get_file_names_without_extension(folder_path)
    n_list = len(s) // thread
    CPU_core = str(CPU_core)
    protein_filename = os.path.splitext(os.path.basename(pdb_file_path))[0]
    st.write("-----设置分子对接目录-----")
    path_analzy = work_dir + "\\" + protein_filename + "\\analzy"  ####需要设置文件夹的路径
    os.makedirs(path_analzy)
    path_analzy3 = work_dir + "\\" + protein_filename + "\\vina_result"
    os.makedirs(path_analzy3)
    for i in range(0, len(s)):
        dirName = str(s[i])
        os.makedirs(path_analzy + "\\" + dirName)  # 批量建立文件夹
    source_dir = work_dir  # 替换为你的源目录路径
    target_dir = work_dir + '/target_folder'  # 替换为你的目标目录路径
    # 确保目标目录存在
    os.makedirs(target_dir, exist_ok=True)
    # 遍历源目录中的所有文件
    st.write("-----需要将受配体文件移动到指定目录，可能需要一点时间......-----")
    for filename in os.listdir(source_dir):
        # 检查文件是否以 .pdb 或 .pdbqt 结尾
        if filename == 'processed_protein.pdb' or filename.endswith('.pdbqt'):
            # 构建完整的源文件路径
            source_file = os.path.join(source_dir, filename)
            # 构建完整的目标文件路径
            target_file = os.path.join(target_dir, filename)
            # 移动文件
            shutil.move(source_file, target_file)
            st.write(f"Moved: {filename}")
    st.write("所有文件移动完成")
    st.write("-----配置vina_config.txt文件，以及驱动程序配置-----")
    for i in range(0, len(s)):
        receptor = receptor_pdbqt  # 需要添加受体名称.pdbqt文件
        ligand = s[i] + ".pdbqt"
        ###确定受体的对接口袋位置
        X1 = "center_x = " + str(center_x)
        Y1 = "center_y = " + str(center_y)
        Z1 = "center_z = " + str(center_z)

        X2 = "size_x = " + str(size_x)
        Y2 = "size_y = " + str(size_y)
        Z2 = "size_z = " + str(size_z)
        # 在小分子文件夹中写入相应的config.txt文件
        lines = ['receptor = ' + receptor, 'ligand = ' + ligand + '\n', X1, Y1, Z1 + '\n', X2, Y2, Z2 + '\n',
                 'energy_range = 5', 'num_modes = 10']
        path_new = work_dir + "\\" + protein_filename + "\\analzy\\" + s[i]
        with open(path_new + "/" + s[i] + "_config.txt", 'w') as file:
            for line in lines:
                file.write(line + '\n')

        cmd = f'qvina2 --config {s[0]}_config.txt --log {s[0]}.txt --out {s[0]}_out.pdbqt --exhaustiveness=8'
        with open(path_new + "/" + "cmd.bat", 'w') as file:
            file.write(cmd)
    for j in range(0, len(s)):
        # 将受体文件和小分子的（.pdbqt文件）移动至各个小分子文件夹
        ligand_DIR = work_dir + '\\ligand_pdbqt'  ####需要移动的原始文件所在路径
        receptor_DIR = work_dir + '\\target_folder'
        move_DIR = work_dir + "\\" + protein_filename + "\\analzy\\" + s[j]  ####希望移动到的新路径。注意：此路径必须存在！！！

        for path, dirs, files in os.walk(receptor_DIR):  # 注意改路径只放受体的pdb文件，和处理好的pdbqt文件

            for file in files:
                file_name = file
                down_file_dir = receptor_DIR + '\\' + file  # 移动前文件
                move_dir_1 = os.path.join(move_DIR, file_name)  # 把目录和文件名合成一个路径
                move_dir_2 = move_DIR + '\\' + file_name
                shutil.copy(down_file_dir, move_dir_2)  # 进行文件移动

        for path, dirs, files in os.walk(ligand_DIR):  # 注意改路径只放小分子的pdbqt文件

            for file in files:
                file_name = file
                ligand_name = file.split('.')[0]
                if ligand_name == s[j]:
                    down_file_dir = ligand_DIR + '\\' + file  # 移动前文件
                    move_dir_1 = os.path.join(move_DIR, file_name)  # 把目录和文件名合成一个路径
                    move_dir_2 = move_DIR + '\\' + file_name
                    shutil.copy(down_file_dir, move_dir_2)  # 进行文件移动
        vina_DIR = work_dir + '\\vina'  ####需要移动的原始文件所在路径
        move_DIR = work_dir + "\\" + protein_filename + "\\analzy\\" + s[j]  ####希望移动到的新路径。注意：此路径必须存在！！！

        for path, dirs, files in os.walk(vina_DIR):  # 注意改路径只放受体的pdb文件，和处理好的pdbqt文件

            for file in files:
                file_name = file
                down_file_dir = vina_DIR + '\\' + file  # 移动前文件
                move_dir_1 = os.path.join(move_DIR, file_name)  # 把目录和文件名合成一个路径
                move_dir_2 = move_DIR + '\\' + file_name
                shutil.copy(down_file_dir, move_dir_2)  # 进行文件移动
    time.sleep(3)
    st.write("-----配置完成-----")
    st.write("-----开始分子对接计算！！！可能需要不少的时间，可以做点别的工作.......-----")
    os.chdir(os.path.join(work_dir, protein_filename, "analzy", s[0]))
    command = f'vina --config {s[0]}_config.txt --log {s[0]}.txt --out {s[0]}_out.pdbqt --exhaustiveness=8'
    # 使用subprocess.run调用CMD并执行命令
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # 检查命令执行结果
    if result.returncode == 0:
        st.write("-----对接计算启动！！！-----")
    else:
        st.write(f"线程【1】{str(s[0])}命令执行失败，返回代码: {result.returncode}")
    st.write("运行完成！！！")
    if thread == 1:

        if __name__ == "__main__":
            # 创建进度条和进度文本
            progress_bar1 = st.progress(0)
            progress_text1 = st.empty()

            # 启动线程
            T1 = threading.Thread(target=run_qvina, args=(s, n_list, 0, len(s), 1, CPU_core), name="T1")

            T1.start()

            while any(t.is_alive() for t in [T1]):
                progress_bar1.progress(progress_values[0])
                progress_text1.text(f"线程【1】进度: {int(progress_values[0] * 100)}%")
                time.sleep(1)

            # 确保所有线程完成
            T1.join()

        time.sleep(10)
    if thread == 2:

        if __name__ == "__main__":
            # 创建进度条和进度文本
            progress_bar1 = st.progress(0)
            progress_text1 = st.empty()
            progress_bar2 = st.progress(0)
            progress_text2 = st.empty()

            # 启动线程
            T1 = threading.Thread(target=run_qvina, args=(s, n_list, 0, n_list, 1, CPU_core), name="T1")
            T2 = threading.Thread(target=run_qvina, args=(s, n_list, n_list - 1, len(s), 2, CPU_core), name="T2")

            T1.start()
            T2.start()

            while any(t.is_alive() for t in [T1, T2]):
                progress_bar1.progress(progress_values[0])
                progress_text1.text(f"线程【1】进度: {int(progress_values[0] * 100)}%")
                progress_bar2.progress(progress_values[1])
                progress_text2.text(f"线程【2】进度: {int(progress_values[1] * 100)}%")
                time.sleep(1)

            # 确保所有线程完成
            T1.join()
            T2.join()

        time.sleep(10)
    if thread == 3:

        if __name__ == "__main__":
            # 创建进度条和进度文本
            progress_bar1 = st.progress(0)
            progress_text1 = st.empty()
            progress_bar2 = st.progress(0)
            progress_text2 = st.empty()
            progress_bar3 = st.progress(0)
            progress_text3 = st.empty()

            # 启动线程
            T1 = threading.Thread(target=run_qvina, args=(s, n_list, 0, n_list, 1, CPU_core), name="T1")
            T2 = threading.Thread(target=run_qvina, args=(s, n_list, n_list - 1, 2 * n_list + 1, 2, CPU_core),
                                  name="T2")
            T3 = threading.Thread(target=run_qvina, args=(s, n_list, 2 * n_list, len(s), 3, CPU_core), name="T3")

            T1.start()
            T2.start()
            T3.start()

            while any(t.is_alive() for t in [T1, T2, T3]):
                progress_bar1.progress(progress_values[0])
                progress_text1.text(f"线程【1】进度: {int(progress_values[0] * 100)}%")
                progress_bar2.progress(progress_values[1])
                progress_text2.text(f"线程【2】进度: {int(progress_values[1] * 100)}%")
                progress_bar3.progress(progress_values[2])
                progress_text3.text(f"线程【3】进度: {int(progress_values[2] * 100)}%")
                time.sleep(1)

            # 确保所有线程完成
            T1.join()
            T2.join()
            T3.join()

        time.sleep(10)
    st.write("所有线程已完成！")
    st.write("------分子对接计算结束，进行结果整理！！！------")
    if __name__ == "__main__":
        M1 = threading.Thread(target=model1, name="M1")
        M1.start()
        M2 = threading.Thread(target=model2, name="M2")
        M2.start()
        M1.join()
        M2.join()
    files_to_delete = [os.path.join(work_dir, r"convert_ligands.bat"),
                       os.path.join(work_dir, "tmp.html")]
    delete_files(files_to_delete)

    vina_result_file_name_list = os.listdir(vina_result_dir)
    vina_result_file_name_list = list(vina_result_file_name_list)
    st.write(
        "本次对接计算共有【" + str(len(s)) + "】个小分子，已经完成【" + str(len(vina_result_file_name_list)) + "】个。")

    ligand_best_dock_list = []
    os.chdir(vina_result_dir)
    for vina_result_file_name in vina_result_file_name_list:
        f = open(vina_result_file_name, 'r', encoding='utf-8')
        vina_content = []
        for lines in f:
            ls = lines.strip(' ').replace('\n', '').split(';')
            for j in ls:
                vina_content.append(j)
        value = vina_content[-11].replace("1        ", "").replace("      0.000      0.000", "").strip(' ')
        ligand_best_dock_list.append((vina_result_file_name.replace(".txt", ""), value))
    ligand_best_dock_list.sort(key=lambda k: float(k[1]))

    os.chdir(protein_dir)
    work_book_file = protein_name + '_result.xlsx'
    if os.path.exists(work_book_file):
        os.remove(work_book_file)
    workbook = xlsxwriter.Workbook(work_book_file)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    worksheet.write(0, 0, "ligand_ID")
    worksheet.write(0, 1, "结合能")

    row = 0
    for ele in ligand_best_dock_list:
        row = row + 1
        worksheet.write(row, 0, ele[0])
        worksheet.write(row, 1, ele[1])
    workbook.close()

    df = pd.read_excel(work_book_file)
    styled_df = df.style.set_properties(**{'width': '150px'})
    st.dataframe(styled_df)

    # 拷贝结合能前 10 的 xxx_out.pdbqt 文件复制到目录 best_10_out 目录中

    st.write("-----分子对接结果已经生成，请查收！感谢使用HTMD v2.0，有问题请联系：geng20210226@163.com")
