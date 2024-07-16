"""
    11 数据类型-布尔类型
"""
# 1 True 和 False 在 python 中是保留关键字，表示布尔值

# 2 布尔类型可以和其他数据类型进行比较、运算时，True 表示 1，false 表示 0
var_bool_true = True
var_bool_false = False
print(var_bool_true + 10)   # 11
print(True + 10)            # 11
print(var_bool_false + 10)  # 10
print(False + 10)           # 10
print("====================================")


# 3 python 中，非 0 被视为 True，0 值被视为 False
if 100:
    print("python bool hello world：100")
if -1:
    print("python bool hello world：-1")
if 1.1:
    print("python bool hello world：1.1")
if "hello":
    print("python bool hello world：\"hello\"")
if 0:
    print(var_false)  # 0 值为 false 不会输出
