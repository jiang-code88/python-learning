"""
    06 数据容器-字符串
     - 字符编码，字符串是由 Unicode 码位构成的不可变序列。
     - 字符串字面值定义：单引号''、双引号""（单/双引号允许嵌套）、三重引号""" """ / ''' '''。
     - 字符串是字符的容器，一个字符串可以存放多个字符串，字符串是字符数组。
     
     - 字符串索引可以从尾部开始取，最后一个元素索引为 -1，往前一位是 -2。
     - 字符串是不可变序列，里面的字符元素不可以被增、删、改。
     
     - python 中字符串的长度没有固定限制，取决于机器的内存有多大。
"""
# 查看字符的 Unicode 码
print(ord('蒋'))
print("="*30)

# 查看 Unicode 码对应的字符
print(chr(49))  # 40 编码对应的字符是 '1'
print("="*30)

# 字符串就是字符数组
str_a = "red-green"
print(str_a)
print(str_a[3])
print("="*30)

# 字符串的遍历
for s in str_a:
    print(s)
print("-"*30)

i = 0
while i < len(str_a):
    print(str_a[i])
    i += 1
print("="*30)

