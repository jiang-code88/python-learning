# 定义类
class Cat:
    # 自定义成员变量，这里定义默认值为 None
    name = None
    age = None
    color = None


def print_cat_obj(cat_obj):
    # 通过 对象.属性名 访问对象的成员变量值
    print(f"cat: 地址：{id(cat_obj)}\n"
          f" name={cat_obj.name}, 地址={id(cat_obj.name)}\n"
          f" age={cat_obj.age}, 地址={id(cat_obj.age)}\n"
          f" color={cat_obj.color}, 地址={id(cat_obj.color)}\n")


if __name__ == '__main__':
    # 创建类的实例对象
    cat = Cat()
    print_cat_obj(cat)

    # 改变对象的成员变量值
    cat.name = "小咪"
    print_cat_obj(cat)
