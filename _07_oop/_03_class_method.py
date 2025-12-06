def hi():
    print("Hello world cat! ")


class Cat:
    name = None
    age = None
    color = None

    """
    自定义成员方法
    
    语法：def 方法名(self 形参列表):
            方法体
        
    self 代表当前对象的本身，定义成员方法时需要写上，如果不写需要标记 @staticMethod 否则报错， 
         在调用对象该成员方法时会被隐式传入，用于访问该对象的成员变量或成员方法（包括类的静态方法）
    """
    def hello(self):
        # 使用 self 调用
        print(f"Hello cat: {self.name}!")
        # 使用 self 调用对象的成员方法
        self.response()
        # 使用 self 调用类的静态方法
        self.staticPet(self.name)

    def response(self):
        print(f"yes i am {self.name}!")

    # @staticmethod 标记 该方法为类的静态方法
    @staticmethod
    def staticPet(name):
        print(f"Static pet cat: {name}!")


if __name__ == '__main__':
    # 使用 对象.方法名 调用对象的成员方法
    cat = Cat()
    cat.name = "小咪"
    cat.hello()
    print("-" * 30)

    # 对象调用类的静态方法
    cat.staticPet("大咪")
    # 还可以类调用类的静态方法
    Cat.staticPet("咪咪")
    print("-" * 30)

    # 动态的为对象添加方法
    # 对对象 cat 添加 hi 方法为其中的 hiMethod (名称自定义)方法，这种添加仅仅是对当前对象的添加。
    cat.hiMethod = hi
    # 调用 hiMethod 相当于调用 hi 方法
    cat.hiMethod()
    print("-" * 30)
