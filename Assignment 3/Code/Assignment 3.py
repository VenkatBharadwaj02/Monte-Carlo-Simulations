import numpy as np
import matplotlib.pyplot as plt
import random
import math as m


L = np.arange(40,161,20)
P = np.arange(0.5,0.7001,0.002)
N=1
pinf = np.zeros((len(L),len(P)))
pinf1 = np.zeros((len(L),len(P)))
csd = np.zeros((len(L),len(P)))
bc = np.zeros((len(L),len(P)))
a = np.zeros((len(L),len(P)))
b = np.zeros((len(L),len(P)))
for n in range(0,N):
    for l in range(0,len(L)):
        for p in range(0,len(P)):
            lat = np.zeros((L[l],L[l]))
            for i in range(0,L[l]):
                for j in range(0,L[l]):
                    rand = random.random()
                    if(rand<P[p]):
                        lat[i][j] = 1
            #print(lat)
            hk = np.zeros((L[l],L[l]), dtype=int)
            mass = [0]
            k=1
            for i in range(0,L[l]):
                for j in range(0,L[l]):
                    if(i==0):
                        if(j==0):
                            if(lat[i][j]):
                                hk[i][j] = k
                                k=k+1
                                mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                                continue
                            else:
                                continue
                        else:
                            if(lat[i][j]):
                                if(lat[i][j-1]):
                                    hk[i][j] = hk[i][j-1]
                                    mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                                    continue
                                else:
                                    hk[i][j] = k
                                    k=k+1
                                    mass = mass + [0]
                                    mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                                    continue
                    if(j==0):
                        if(lat[i][j]):
                            if(lat[i-1][j]):
                                hk[i][j] = hk[i-1][j]
                                mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                                continue
                            else:
                                hk[i][j] = k
                                k=k+1
                                mass = mass + [0]
                                mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                                continue
                    if(lat[i][j]):
                        if(lat[i-1][j]):
                            if(lat[i][j-1]):
                                if(hk[i][j-1]== hk[i-1][j]):
                                    hk[i][j] = hk[i-1][j]
                                    mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                                    continue
                                tmp = mass[hk[i-1][j]-1]
                                tmp1= hk[i-1][j]
                                while(tmp<0):
                                    tmp1=tmp
                                    tmp = mass[abs(tmp1)-1]
                                tmp = mass[hk[i][j-1]-1]
                                tmp2= hk[i][j-1]
                                while(tmp<0):
                                    tmp2=tmp
                                    tmp = mass[abs(tmp2)-1]
                                if(abs(tmp1)==abs(tmp2)):
                                    hk[i][j] = abs(tmp1)
                                    mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                                else:
                                    hk[i][j] = min(abs(tmp1),abs(tmp2))
                                    mass[hk[i][j]-1] = mass[abs(tmp1)-1]+mass[abs(tmp2)-1]+1
                                    mass[max(abs(tmp1),abs(tmp2))-1] = -1*hk[i][j]
                            else:
                                tmp = mass[hk[i-1][j]-1]
                                tmp1=hk[i-1][j]
                                while(tmp<0):
                                    tmp1 = tmp
                                    tmp = mass[abs(tmp1)-1]
                                hk[i][j] = abs(tmp1)
                                mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                        elif(lat[i][j-1]):
                            tmp = mass[hk[i][j-1]-1]
                            tmp1= hk[i][j-1]
                            while(tmp<0):
                                tmp1 = tmp
                                tmp = mass[abs(tmp1)-1]
                            hk[i][j] = abs(tmp1)
                            mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
                        else:
                            hk[i][j] = k
                            k=k+1
                            mass = mass+[0]
                            mass[hk[i][j]-1] = mass[hk[i][j]-1]+1
            s = []
            ns = []
            for t in range(0,len(mass)):
                if(mass[t]>0):
                    if (mass[t] in s):
                        ns[s.index(mass[t])] = ns[s.index(mass[t])]+1
                    else:
                        s = s+[mass[t]]
                        ns = ns+[1]
            #print(s,ns)
            perc = set()
            for i in range(0,L[l]):
                if(hk[0][i]!=0):
                    for j in range(0,L[l]):
                        if(hk[L[l]-1][j] == hk[0][i]):
                            perc.add(hk[0][i])
            #print(perc)
            pinf1[l][p] = P[p]
            for i in perc:
                pinf[l][p] = pinf[l][p]+mass[i-1]/(L[l]*L[l])
                pinf1[l][p] = pinf1[l][p]+mass[i-1]/(L[l]*L[l])
            for i in range(0,len(s)):
                pinf1[l][p] = pinf1[l][p]-s[i]*ns[i]/(L[l]*L[l])
                csd[l][p] = csd[l][p]+s[i]*s[i]*ns[i]
            a[l][p] = a[l][p]+pinf[l][p]*pinf[l][p]*pinf[l][p]*pinf[l][p]/N
            b[l][p] = b[l][p]+pinf[l][p]*pinf[l][p]/N        
        #print(pinf,pinf1)
    print(n)
pinf = pinf/N
pinf1 = pinf1/N
csd = csd/N
bc = 3/2*(1-a/(3*b*b))
for i in range(0,3):
    plt.plot(P,pinf[i])
plt.show()
for i in range(0,len(L)):
    plt.scatter(P,pinf1[i],s=0.5)
plt.show()
for i in range(0,len(L)):
    plt.scatter(P,csd[i],s=0.5)
plt.show()
for i in range(0,len(L)):
    plt.scatter(P,bc[i],s=0.5)
plt.show()

