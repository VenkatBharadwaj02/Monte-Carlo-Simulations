import numpy as np
import random
import math as m
import matplotlib.pyplot as plt
from itertools import product, combinations

R = 1+random.random()
L = 20*R

Nmax = int(L**3*0.74*3/(4*m.pi*R**3))
#print(R,L,Nmax)

M = 1
N = np.zeros((M))
rmean = np.zeros((M))

for i in range(M):
    reject=0
    accept=0
    spheres = [[R+(L-2*R)*random.random(),R+(L-2*R)*random.random(),R+(L-2*R)*random.random()]]

    while(reject<10*Nmax):
        tmp=0
        rm = 0
        x1 = R+(L-2*R)*random.random()
        y1 = R+(L-2*R)*random.random()
        z1 = R+(L-2*R)*random.random()
        for sphere in spheres:
            r = m.sqrt((x1-sphere[0])**2+(y1-sphere[1])**2+(z1-sphere[2])**2)
            if(r>=2*R):
                rm = rm+r
            else:
                tmp = 1
                break
        if(tmp):
            reject = reject+1
        else:
            reject=0
            accept = accept+1
            rmean[i] = rmean[i]+rm
            spheres = spheres+[[x1,y1,z1]]
    N[i] = accept
    rmean[i] = 2*rmean[i]/(N[i]*(N[i]-1))

print(N)
print(rmean)

fig = plt.figure()


ax = fig.add_subplot(projection='3d')
r = [0, L]
for s, e in combinations(np.array(list(product(r, r, r))), 2):
   if np.sum(np.abs(s-e)) == r[1]-r[0]:
      ax.plot3D(*zip(s, e), color="black")
for sphere in spheres:
    ax.scatter(sphere[0], sphere[1], sphere[2], c='y', s=10)

plt.show()