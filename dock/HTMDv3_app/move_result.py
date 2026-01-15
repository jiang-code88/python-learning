import os
import shutil
import threading

import xlsxwriter

work_dir = r"D:\dock\TEXT8_2GW5_32"
protein_filename = "protein"
protein_dir = os.path.join(work_dir, protein_filename)
ligand_pdbqt_dir = os.path.join(work_dir, "ligand_pdbqt")
vina_result_dir = os.path.join(protein_dir, 'vina_result')


def get_file_names_without_extension(folder_path):
    file_names = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            name_without_extension = os.path.splitext(file_name)[0]
            file_names.append(name_without_extension)
    return file_names


ligand_file_name_list = get_file_names_without_extension(ligand_pdbqt_dir)


def move_result():
    for ligand_file_name in ligand_file_name_list:
        ligand_result_dir = os.path.join(protein_dir, 'analzy', ligand_file_name)
        result_file_list = os.listdir(ligand_result_dir)
        for result_file in result_file_list:
            if result_file == ligand_file_name + ".txt":
                shutil.copy(os.path.join(ligand_result_dir, result_file), vina_result_dir)
                print(f"[copy] 将 {os.path.join(ligand_result_dir, result_file)} 文件拷贝到目录 {vina_result_dir}")


def delete_files(files):
    for file in files:
        file_path = os.path.join(work_dir, file)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"[remove] 删除文件 {file}")
        else:
            print(f"[remove] 文件 {file} 不存在")


if __name__ == "__main__":
    M1 = threading.Thread(target=move_result, name="M1")
    M1.start()
    M1.join()

    files_to_delete = [os.path.join(work_dir, r"convert_ligands.bat"), os.path.join(work_dir, "tmp.html")]
    delete_files(files_to_delete)

    vina_result_file_name_list = os.listdir(vina_result_dir)
    vina_result_file_name_list = list(vina_result_file_name_list)
    print("本次对接计算共有【" + str(len(ligand_file_name_list)) + "】个小分子，已经完成【" + str(
        len(vina_result_file_name_list)) + "】个。")

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

    ligand_best_dock_list.sort(key=lambda x: float(x[1]))

    os.chdir(protein_dir)
    work_book_file = protein_filename + '_result.xlsx'
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
