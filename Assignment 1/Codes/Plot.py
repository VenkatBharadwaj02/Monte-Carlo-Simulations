import numpy as np
import matplotlib.pyplot as plt

arr1 = np.loadtxt("D:\Academics\Engineering Physics\Sem-7\PH415\Assignments\Assignment 1\B.csv",delimiter=",", dtype=float)

plt.plot(arr1[:,1], arr1[:,0])
plt.title('Average Spacing vs. Radius of Spheres')
plt.xlabel('Average Spacing')
plt.ylabel('Radius of Spheres')
plt.show()

arr2 = np.loadtxt("D:\Academics\Engineering Physics\Sem-7\PH415\Assignments\Assignment 1\C.csv",delimiter=",", dtype=float)

plt.plot(arr2[:,0], arr2[:,1])
plt.title('Consecutive Failures vs. Number of Spheres')
plt.ylabel('Number of Spheres')
plt.xlabel('Consecutive Failures (in units of Nmax)')
plt.show()