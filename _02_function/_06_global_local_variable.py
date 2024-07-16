"""
    06 全局变量和局部变量
    全局变量：在整个程序范围内都可以访问，定义在函数外，拥有全局作用域的变量
    局部变量：只能在其被声明的函数范围内访问，定义在函数内，拥有局部作用域的变量

    注意事项：
     1 未在函数内部重新定义变量的局部变量，函数内默用使用函数外定义的全局变量。
       如果在函数内部重新定义变量的局部变量，按就近原则，函数内将使用函数内部重新定义的局部变量。
     2 在函数内部使用 global 全局变量名 标明函数可以直接操作（读写）全局变量
"""
# 全局变量 n1
n1 = 100


def f1():
    # 局部变量 n2
    n2 = 200
    # 函数内部可以访问局部变量
    print(f"function scope access local variable n2: {n2}")
    # 函数内部可以访问全局变量
    print(f"function scope access global variable n1: {n1}")


# 调用函数
f1()

# 函数外可以访问全局变量
print(f"global scope access global variable n1: {n1}")

# 函数外不可以访问局部变量
# print(n2)
print("===============================")


def f2():
    # 重新定义全局变量 n1 为局部变量 n1
    n1 = 300
    print(f"function scope access global to local variable n1: {n1}")


def f3():
    global n1
    print(f"function scope access global variable n1: {n1}")
    n1 = 400
    print(f"function scope update global variable n1: {n1}")


# 函数内对全局变量的重新定义不会影响全局变量原始的值
f2()
print(f"global scope access global variable n1: {n1}")
# 函数内使用 global 关键字标明函数可以直接操作（读写）全局变量 n1
f3()
print(f"global scope access function update global variable n1: {n1}")
print("================================")
