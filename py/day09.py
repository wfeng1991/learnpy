import os

print(os.name)

# print(os.environ)

print(os.path.split('/Users/michael/testdir/file.txt'))

print(os.path.splitext('/path/to/file.txt'))

# os.rename('test.txt', 'test.py')

# os.remove('test.py')

l = [x for x in os.listdir('.')]

print(l)