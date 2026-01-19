# 展示所有构象
split_states ligand

# 给所有构想添加氢键
distance hbonds, protein, ligand_0001, mode=2
distance hbonds, protein, ligand_0002, mode=2
distance hbonds, protein, ligand_0003, mode=2
distance hbonds, protein, ligand_0004, mode=2
distance hbonds, protein, ligand_0005, mode=2
distance hbonds, protein, ligand_0006, mode=2
distance hbonds, protein, ligand_0007, mode=2
distance hbonds, protein, ligand_0008, mode=2
distance hbonds, protein, ligand_0009, mode=2
distance hbonds, protein, ligand_0010, mode=2

# 删除构想
delete ligand_0002
delete ligand_0003
delete ligand_0004
delete ligand_0005
delete ligand_0006
delete ligand_0007
delete ligand_0008
delete ligand_0009
delete ligand_0010

