kvar=15
for ivar in range(7,5,-1):
    kvar-=ivar
    print(kvar)
print(kvar)


animallist=[ ["Persian", "Siamese", "Calico"], ["Quarterhorse", "Arabian", "Haflinger", "Morgan"], ["Chow", "Boxer"] ]

print(animallist[0][-2:])


import numpy as np
myarray=np.zeros((3,2,2,3))

print(myarray.ndim)

A=np.array([[2,-1],[0,2]])
B=np.array([[3,-1],[1,1]])
C=A/B

print(C)