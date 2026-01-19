# 载入蛋白质和小分子构像
load D:\dock\TEXT6_AF-Q8N423-F1-model_v6\AF-Q8N423-F1-model_v6.pdb, protein
load D:\dock\TEXT6_AF-Q8N423-F1-model_v6\AF-Q8N423-F1-model_v6\analzy\441336\441336_out.pdbqt, ligand

# 背景设置白色
bg_color white

# 隐藏所有
hide everything

# 蛋白质样式显示 cartoon
show cartoon, protein
# 蛋白质颜色显示 gray70
color gray70, protein
# 蛋白质透明度变成 80%
set cartoon_transparency, 0.8, protein

# 小分子样式显示 sticks
show sticks, ligand
color atomic, ligand

# 添加氢键
distance hbonds, protein, ligand, mode=2

show lines, protein

# 自己手选蛋白残基，蛋白质转 cartoon
# show sticks, sele
# util.cbag sele
# label sele and name CA, "%s-%s" % (resn, resi)
# set label_size, 16

