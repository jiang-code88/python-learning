"""
    02 导入模块
    导入模块的语法：[from 模块名] import (函数｜类｜变量｜*) [as 别名]
     - [] 代表可选（可有可无）项目、() 代表必填项目、｜ 代表可选（其中一个）项目。
"""
# 模块导入形式一（直接导入模块）
# import 模块名
# import 模块名_1, 模块名_2, ...
# 使用 模块名.xx 来使用导入的模块中的 xx 功能
# import math
# print(math.fabs(-11.2))  # 返回 -11.2 的绝对值


# 模块导入形式二（导入模块的指定功能）
# from 模块 import 函数、类、变量...
# 这种方式的好处是导入具体的函数、类、变量后，直接使用即可，无需再带模块名使用
# from math import fabs
# print(fabs(-11.2))  # 返回 -11.2 的绝对值


# 模块导入形式三（导入模块的所有功能）
# from math import *
# print(sqrt(4))  # 返回 4 的平方根


# 模块导入形式三（给导入的模块取别名）
# import 模块名 as 别名
# from 模块名 import 函数、类、变量... as 别名
import random as r
print(r.choice(['a', 'b', 'c']))
from math import sqrt as sq
print(sq(16))

