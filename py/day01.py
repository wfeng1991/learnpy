

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列

for i in primes():
    if i < 1000:
        print(i)
    else:
        break


def count():
    fs = []
    for i in range(1, 4):
        def g(x):
            def f():
                return x*x
            return f
        fs.append(g(i))
    return fs

f1, f2, f3 = count()
print([f1(), f2(), f3()])
