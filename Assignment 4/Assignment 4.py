import numpy as np
import matplotlib.pyplot as plt
import math as m
import random
import seaborn as sns

Tc = 2/(m.log(1+m.sqrt(2)))
L = 128
Temp = [1.5,Tc,3]#np.arange(1.25,3.26,0.05)

lat = np.random.choice([-1,1],size=(L,L))
e = np.zeros((L,L))
tmax = 500
E = np.zeros((tmax))
mag = np.zeros((tmax))
E2avg = np.zeros((len(Temp)))
Eavg = np.zeros((len(Temp)))
mavg = np.zeros((len(Temp)))
m2avg = np.zeros((len(Temp)))
sus = np.zeros((len(Temp)))
sh = np.zeros((len(Temp)))

for k in range(0,len(Temp)):
    count = 0
    t=0
    while t<tmax:
        for i in range(0,L):
            for j in range(0,L):
                e[i,j] = -lat[i,j]*(lat[(i-1)%L,j]+lat[i,(j-1)%L]+lat[(i+1)%L,j]+lat[i,(j+1)%L])
                dE = -2*e[i,j]
                p = m.exp(-dE/Temp[k])
                r = random.random()

                #print(p,r)
                if(r<=p):
                    lat[i,j] = -lat[i,j]
        #print(lat)
        mag[t] = abs(sum([tmp for tmp in sum(lat)])/(L*L))
        E[t] = sum([tmp for tmp in sum(e)])/2

        if(t>1000 and t%100==0):
            count = count+1
            Eavg[k] = Eavg[k] + E[t]
            mavg[k] = mavg[k] + mag[t]
            E2avg[k] = E2avg[k] + E[t]*E[t]
            m2avg[k] = m2avg[k] + mag[t]*mag[t]

        print(t)
        t=t+1
    
    plt.plot(np.arange(0,tmax,1),mag)
    plt.show()
    plt.plot(np.arange(0,tmax,1),E)
    plt.show()
    sns.heatmap(lat)
    plt.show()

Eavg = Eavg/count
mavg = mavg/count
m2avg = m2avg/count
E2avg = E2avg/count

for i in range(0,len(Temp)):
    sus[i] = L*L/Temp[i]*(m2avg[i]-mavg[i]^2)
    sh[i] = 1/(Temp[k]*Temp[k])*(E2avg[i]-Eavg[i]^2)

plt.plot(Temp,mavg)
plt.show()
plt.plot(Temp,Eavg)
plt.show()
plt.plot(Temp,sus)
plt.show()
plt.plot(Temp,sh)
plt.show()
