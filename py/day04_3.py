# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        def add(self,value):
            self.append(value)
        attrs['add'] = add
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
for i in l:
    print(i)