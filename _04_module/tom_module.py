"""
    自定义子模块
"""
__all__ = ['hi']  # 限定使用 from xxx import * 导入该模块时，只能导入 hi 方法


def hi():
    print('tom hi')


# 模块内的可执行代码只有在模块被执行时（__name__变量值为 '__main__'）才会执行
# 被导入时不会执行（__name__ 变量值为模块名  'tom_module'）
if __name__ == '__main__':
    hi()
    print("tom other hi")
