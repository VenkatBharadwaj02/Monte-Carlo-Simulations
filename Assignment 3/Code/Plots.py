from cProfile import label
from operator import le
import numpy as np
import matplotlib.pyplot as plt
import math as m

L = [40,60,80,100,120,140,160]
P = np.arange(0.5,0.701,0.002)
x = np.zeros((len(L)))
y = np.zeros((len(L)))

Pinf = np.loadtxt("D:\Academics\Engineering Physics\Sem-7\PH415\Assignments\Assignment 3\Pinf.csv",delimiter=",", dtype=float)
csd = np.loadtxt("D:\Academics\Engineering Physics\Sem-7\PH415\Assignments\Assignment 3\csd.csv",delimiter=",", dtype=float)
bc = np.loadtxt("D:\Academics\Engineering Physics\Sem-7\PH415\Assignments\Assignment 3\Bc.csv",delimiter=",", dtype=float)

pc = 0.596
Pinf_pc = Pinf[:,int((pc-0.5)/0.002)]
for i in range(0,len(L)):
    y[i] = m.log(Pinf_pc[i])
    x[i] = m.log(L[i])
plt.scatter(x,y)
z = np.polyfit(x,y, 1)
p = np.poly1d(z)
bn = -z[0]
plt.plot(x, p(x), linestyle="--", label='Slope = '+str(np.round(z[0],3)))
plt.title('Log-Log Scale Plot of P_inf at Percolation Threshold vs. Lattice Size')
plt.ylabel('log(P_inf(p=p_c,L))')
plt.xlabel('log(L)')
plt.legend()
plt.show()

chi_pc = csd[:,int((pc-0.5)/0.002)]
for i in range(0,len(L)):
    y[i] = m.log(chi_pc[i])
    x[i] = m.log(L[i])
plt.scatter(x,y)
z = np.polyfit(x,y, 1)
p = np.poly1d(z)
gn = z[0]
plt.plot(x, p(x), linestyle="--", label='Slope = '+str(np.round(z[0],3)))
plt.title('Log-Log Scale Plot of Chi at Percolation Threshold vs. Lattice Size')
plt.ylabel('log(Chi(p=p_c,L))')
plt.xlabel('log(L)')
plt.legend()
plt.show()

dU_pc = (bc[:,int((pc-0.5)/0.002)]-bc[:,int((pc-0.5)/0.002)-1])/0.002
for i in range(0,len(L)):
    y[i] = m.log(dU_pc[i])
    x[i] = m.log(L[i])
plt.scatter(x,y)
z = np.polyfit(x,y, 1)
p = np.poly1d(z)
nu = 1/z[0]
plt.plot(x, p(x), linestyle="--", label='Slope = '+str(np.round(z[0],3)))
plt.title('Log-Log Scale Plot of dU/dp at Percolation Threshold vs. Lattice Size')
plt.ylabel('log(dU(p,L)/dp)|p=p_c')
plt.xlabel('log(L)')
plt.legend()
plt.show()

for i in range(0,len(L)):
    x = np.zeros((len(P)))
    y = Pinf[i,:]
    for j in range(0,len(P)):
        x[j] = (P[j]-pc)*m.pow(L[i],1/nu)
        y[j] = y[j]*m.pow(L[i],bn)

    plt.plot(x,y, label='L = '+str(L[i]))
plt.title('Rescaled Plot of P_inf(p,L) vs p for various L')
plt.xlabel(r"$z = (p-p_c)*L^{1/\nu}$")
plt.ylabel(r"$L^{\beta/\nu}P_\infty$")
plt.legend()
plt.show()

for i in range(0,len(L)):
    x = np.zeros((len(P)))
    y = csd[i,:]
    for j in range(0,len(P)):
        x[j] = (P[j]-pc)*m.pow(L[i],1/nu)
        y[j] = y[j]*m.pow(L[i],-gn)

    plt.plot(x,y, label='L = '+str(L[i]))
plt.title('Rescaled Plot of Chi(p,L) vs p for various L')
plt.xlabel(r"$z = (p-p_c)*L^{1/\nu}$")
plt.ylabel(r"$L^{-\gamma/\nu}\chi$")
plt.legend()
plt.show()

for i in range(0,len(L)):
    x = np.zeros((len(P)))
    y = bc[i,:]
    for j in range(0,len(P)):
        x[j] = (P[j]-pc)*m.pow(L[i],1/nu)
        y[j] = y[j]

    plt.plot(x,y, label='L = '+str(L[i]))
plt.title('Rescaled Plot of U(p,L) vs p for various L')
plt.xlabel(r"$z = (p-p_c)*L^{1/\nu}$")
plt.ylabel(r"$U(p,L)$")
plt.legend()
plt.show()