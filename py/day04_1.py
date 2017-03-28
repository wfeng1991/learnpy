class Animal(object):

    def run(self):
        print('animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):

    def run(self):
        print('cat is running...')

dog = Dog()
cat = Cat()
# dog.run()
# cat.run()


def run_twice(Animal):
    Animal.run()
    Animal.run()
run_twice(cat)


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

    def print_self(self):
        print("name:%s " % self.name)

s1 = Student()
s1.name = 'wfeng'
s1.age = 25
s1.print_self()
