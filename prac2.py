import numpy as np
import math
#option a
li=[];
li.append(np.random.randint(1,1000,4000))
ar=np.array(li)
ar=np.reshape(ar,(100,40))
print(np.mean(ar,1))
print(np.var(ar,1))
print(np.std(ar,1))
#option b
b=[56,32,23,131,42,141,415,67]
a=b.copy()
a.sort()
li4=[]
for i in b:
   li4.append({i:a.index(i)})
print(li4)
#option c
li5=[]
m=int(input("Enter m"))
n=int(input("Enter n"))
li5.append(np.random.randint(1,100,m*n))
arr=np.array(li5)
arr=np.reshape(arr,(m,n))
print(arr.shape,arr.dtype,arr)
arr=np.reshape(arr,(n,m))
print(arr.shape,arr.dtype,arr)
#option 4
li3=[]
li3.extend([0,0,0,0,0])
li3.extend(np.random.randint(-15,15,10))
li3.extend([np.nan,np.nan,np.nan,np.nan,np.nan])
np.random.shuffle(li3)
zero=[]
nzero=[]
nan=[]
j=0;
for i in li3:
    if math.isnan(i): nan.append(j)
    elif i==0 : zero.append(j)
    else : nzero.append(j)
    j=j+1
print(li3,zero,nzero,nan)

