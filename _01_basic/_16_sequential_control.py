"""
    01 程序流程控制
     - 顺序控制
     - 分支控制
        - 单分支 if
        - 双分支 if-else
        - 多分支 if-elif-else
        - 嵌套分支（多重分支）
     - 循环控制
        - for 循环
         - for-else
        - while 循环
         - while-else
        - 多重循环
        - break 语句
        - continue 语句
        - return 语句
"""
# 分支控制
age = 5
if age > 10:
    print('c')
elif age > 20:
    print('d')
else:
    print('e')
print("===================")
# 其他编程语言的代码块使用 {} 表示的，python 使用缩减代替 {} 表示代码块


# 循环控制
# for 循环
nums = [100, 101, 102, 103, 104]
for var in nums:
    print(var)
# 使用内置 range() 函数，生成数列
for var in range(5):  # 默认从 0 开始，步长为 1
    print(var)
for var in range(4, 5):  # 前闭后开，步长为 1
    print(var)
for var in range(8, 11, 2):  # 步长为 2
    print(var)
# for + else 配合使用
for var in range(55, 57):
    print(var)
    # if var == 56:
    #     break
else:
    # else 中的语句只有在 for 循环正常运行结束后才执行（break 语句执行时，else 不会执行）
    print("for-normal-end")
print("for-end")
print("===================")

# while 循环（在表达式为真时，重复循环的执行语句，在表达式为假时，退出 while 循环）
v = 1
while v <= 3:
    print(v)
    v += 1
# while + break 配合使用
v1 = 1
while v1 <= 3:
    print(v1)
    # if v1 == 3:
    #     break
    v1 += 1
else:
    print("while-normal-end")
print("while-end")
print("===================")

# break 语句
# break 语句用在 for 或 while 循环所嵌套的代码
# break 语句用于终止最近的外层循环，如果循环有可选的 else 子句，也会跳过该子句
# 统计随机生成 1-100 的随机数，直到生成 97，用了多少次
import random

count = 0
while True:
    num = random.randint(1, 100)
    count = count + 1
    if num == 97:
        break
print(count)
print("===================")

# continue 语句
# continue 语句用在 for 或 while 循环所嵌套的代码
# continue 语句用于结束本次循环，继续执行循环的下一轮次
for i in range(1, 4):
    if i == 2:
        continue
    print(i)
print("===================")


# return 语句
# return 语句使用在函数，表示跳出所在的函数
def f1():
    for v in range(1, 4):
        if v == 2:
            return
        print(v)
    print("=======f1 end=======")

# 调用函数
f1()
