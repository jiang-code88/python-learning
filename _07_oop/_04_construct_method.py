class Cat:
    name = None
    age = None
    color = None

    """
    自定义构造方法
    
    语法：def __init__(self 形参列表):
            方法体
        
    构造方法不能有返回值，否则会报错
    """
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        print("Cat object created")


class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        print("Dog object created")


def print_cat_obj(cat_obj):
    print(f"cat: 地址：{id(cat_obj)}\n"
          f" name={cat_obj.name}, 地址={id(cat_obj.name)}\n"
          f" age={cat_obj.age}, 地址={id(cat_obj.age)}\n"
          f" color={cat_obj.color}, 地址={id(cat_obj.color)}\n")


if __name__ == '__main__':
    # 调用构造方法创建对象
    cat = Cat("老咪", 30, "blue")
    print_cat_obj(cat)

    # 使用构造方法可以动态的生成对象的成员变量
    dog = Dog("旺财", 10, "red")
    print_cat_obj(dog)
