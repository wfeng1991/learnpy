import pickle

d = dict(name='Bob',age=25,score=90)
f = pickle.dumps(d)
print(f)

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()

print(d)

print(u'成都市')