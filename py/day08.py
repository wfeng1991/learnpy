from io import StringIO

f = StringIO()

f.write("hello")
f.write(" ")
f.write("world")

print(f.getvalue())

ff = StringIO('Hello!\nHi!\nGoodBye!')
while True:
    line = ff.readline()
    if line == '':
        break
    print(line.strip())

from io import BytesIO

fff = BytesIO()

fff.write('你好'.encode('utf-8'))

print(fff.getvalue())

ffff = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(ffff.read())
