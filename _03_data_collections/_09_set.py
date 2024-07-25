"""
    09 python 集合
     集合是由不重复元素组成的无序容器，集合对象支持合集、交集、差集等数学运算。

     - 集合定义
     - 集合使用
     - 创建空集合
"""
# 集合的定义
set_a = {100, 200, 300, 400, 500}
print(f"集合的内容：{set_a} 集合的类型：{type(set_a)}")
print("="*30)

# 集合中存储重复元素时，会自动去重
set_b = {100, 200, 300, 400, 500, 500, 200}
print(f"集合的内容：{set_b} 集合的类型：{type(set_b)}")
print("="*30)

# 遍历集合元素（只支持使用 for 循环遍历）
for i in set_a:
    print(i)
print("="*30)

# 创建空集合
set_empty = set()
print(f"集合的内容：{set_empty} 集合的类型：{type(set_empty)}")
