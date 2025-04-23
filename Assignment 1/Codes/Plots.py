import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt("D:\Academics\Engineering Physics\Sem-7\PH415\Assignments\Assignment 1\Data1.csv",delimiter=",", dtype=float)
print('Mean of Average Spacing = ', np.mean(arr[:,1]))
print('Standard Deviation of Average Spacing = ', np.std(arr[:,1]))
print('Mean of Number of Spheres = ', np.mean(arr[:,0]))
print('Standard Deviation of Number of Spheres = ', np.std(arr[:,0]))
'''
hist1, bins1 = np.histogram(arr[:,1], bins=100)
center = (bins1[:-1] + bins1[1:]) / 2
plt.bar(center, hist1, align='center')
plt.title('Frequency of Average Spacing')
plt.ylabel('Frequency')
plt.xlabel('Average Spacing')
plt.show()

hist2, bins2 = np.histogram(arr[:,0], bins=100)
center = (bins2[:-1] + bins2[1:]) / 2
plt.bar(center, hist2, align='center')
plt.title('Frequency of Number of Spheres')
plt.ylabel('Frequency')
plt.xlabel('Number of Spheres')
plt.show()

arr = arr[arr[:,1].argsort()]
plt.scatter(arr[:,1], arr[:,0], s=1)
plt.title('Average Spacing vs. Number of Spheres')
plt.xlabel('Average Spacing')
plt.ylabel('Number of Spheres')
plt.show()
'''