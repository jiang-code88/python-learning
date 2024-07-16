"""
    09 基本数据类型-整数
"""
import sys

# 1 整数的表示
# 十进制
print(10)
# 八进制
print(0o10)
# 十六进制
print(0x10)
# 二进制
print(0b10)
print("=============")


# 2 整数的存储
# python 整型使用 28 个字节存储数据，
# 同时存储所用字节数会随着数值的增大而增大（每次的增量单位是 4 个字节）
print(0, sys.getsizeof(0), type(0))
print(1, sys.getsizeof(1), type(1))
print(2**30, sys.getsizeof(2**30), type(2**30))  # 2 的 32 次方
print(2**80, sys.getsizeof(2**80), type(2**80))  # 2 的 80 次方
