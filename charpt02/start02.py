#coding:utf-8

import pickle

with open("a.pickle","wb") as f:
    pickle.dump(["1",2,"3"],f)
with open("a.pickle","rb") as f:
    da=pickle.load(f)
    print(da)

p=[1,1,2,2,3,4,5,6,8,0,10,15]
m=sorted(set(p))




f="a"
print(type(m))