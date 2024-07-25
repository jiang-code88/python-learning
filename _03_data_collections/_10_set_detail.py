"""
    10 python 集合常用操作
    - 并集
    - 交集
    - 差集

    集合生成式
     - 语法：{集合元素的表达式 for 自定义变量 in 可迭代对象}
"""
# 并集
set_a = {'a', 'b', 'c'}
set_b = {'c', 'd', 'e'}
set_union = set_a.union(set_b)
set_union_brief = set_a | set_b  # 求并集的简单写法
print(f"原始集合 set_a：{set_a}, 原始集合 set_b：{set_b}, 并集 set_union：{set_union}")
print("="*30)

# 交集
set_intersection = set_a.intersection(set_b)
set_intersection_brief = set_a & set_b
print(f"原始集合 set_a：{set_a}, 原始集合 set_b：{set_b}, 交集 set_intersection：{set_intersection}")
print("="*30)

# 差集
set_difference = set_a.difference(set_b)
set_difference_brief = set_a - set_b
print(f"原始集合 set_a：{set_a}, 原始集合 set_b：{set_b}, 差集 set_difference：{set_difference}")
print("="*30)

# 集合生成式
set_c = {ele * 2 for ele in range(1, 5)}
print(f"set_c：{set_c}")
