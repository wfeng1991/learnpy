def func(a):
    return a*a
print(func(2))
def fbonaq(n):
    if n <3:
        return n
    else:
        return fbonaq(n-2)+fbonaq(n-1)
print(fbonaq(4))
a = [1,2,3,4,5,6,7]

def som(a, b=9):
    return a*b
print(som(3))
print(som(3,4))
    