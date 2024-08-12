"""
    03 包中 __init__.py 文件使用
"""
# __init__.py 用于针对 from 包名 import * 的导入方式，
# 控制允许导入的包中模块(默认这样导入是不会导入任何包中模块的)
# __init__.py 文件控制对于 import xxx 的导入方式不起作用。
from my_package import *
module02.hi()
module01.ok()



