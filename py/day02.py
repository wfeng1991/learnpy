def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()

L = [x*x for x in range(10)]
print(L)
g = (x * x for x in range(10))

#杨辉三角
def triangles():
    n = [1]
    yield n
    while True:
        l = len(n)
        idx = 0
        a = []
        while idx <= l:
            if idx == 0 or idx == l:
                a.append(1)
            else:
                a.append(n[idx-1]+n[idx])
            idx = idx +1
        n = a
        yield n

b = triangles()
c = 0
while c < 10:
    c = c+1
    print(next(b))
