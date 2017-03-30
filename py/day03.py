from functools import reduce
import functools

def add(a,b,f):
    return f(a)+f(b)
c = add(5,-5,abs)
#print(c)


a = [x for x in range(10)]
b = map(lambda x:x*x,a)
# for c in b:
#     print(c)


c = reduce(lambda x,y:x+y,a)
#print(c)


def fn(a,b):
    return a*10+b
def strToNum(n):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[n]
def toInt(str):
    return reduce(fn,map(strToNum,str))
# print(toInt('13254354'))

# print(chr(1111))

def normalize(name):
    return name.title()
l = map(normalize,['adam', 'LISA', 'barT'])
# print(list(l))

# print(reduce(lambda x,y:x*y,[1,3,5]))
a = ['bob', 'about', 'Zoo', 'Credit']
a = sorted(a, key=str.lower)
# print(a)
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sorter(a):
    return a[1]
L = sorted(L,key=sorter)
# print(L)

def log(func):
    def wrapper():
        print('call %s():' % func.__name__)
        return func()
    return wrapper
@log
def now():
    print('2015-3-25')
# now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('before %s %s():' % (text, func.__name__))
            r = func(*args, **kw)           
            print('after %s %s():' % (text, func.__name__))
            return r
        return wrapper
    return decorator
@logger('test')
def f():
    print('hello')
f()
@logger('test')
def fp(x,y):
    print('计算xy之和')
    return x+y
a = fp(3,5)
print(a)
