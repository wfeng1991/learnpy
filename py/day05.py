from hello import Hello

h = Hello()
print(h)


def fn(self, name='world'):  # 先定义函数
    print('Hi, %s.' % name)

Hi = type('Hi',(object,),dict(hello=fn))
hi = Hi()
hi.hello()
