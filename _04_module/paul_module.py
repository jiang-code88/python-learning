"""
    自定义子模块
"""


def hi():
    print('paul hi')


# paul_module 模块的可执行代码，import 该模块时该段代码将自动被执行
hi()
print("paul other hi")

# 模块被导入时 __name__ 变量值是 'paul_module'
# 模块被执行时 __name__ 变量值是 '__main__'
print(__name__)
