"""
    03 自定义模块
    - 在 from math import * 时会执行导入模块内的函数调用，因此在每个模块中判断 __name__ == "__main__"，
    确保只有最顶层主程序的函数调用会被执行，处于被导入模块的函数调用不会被执行。
    主程序的 __name__ 是 "__main__"，被导入模块的 __name__ 是模块(文件)去掉 .py 后缀后的名字

    - 在 from math import * 时，可以在被导入的模块中通过 __all__ 限制只允许那些模块功能可以被导入。
      __all__['函数名_1', '函数名_2',...]
      注意：import 模块名 的导入模块形式，不受 __all__ 限制。

"""
