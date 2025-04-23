import numpy as np
import matplotlib.pyplot as plt
import random
import math as m
import seaborn as sns

B = [0.5,0.75,1]
Ns = 100#int(10000 + 10000*random.random())
N = int(40000 + 10000*random.random())
re = np.zeros((Ns,len(B)))

for k in range(len(B)): 
    p_a  = 1/4*(1-B[k])
    p_c = 1/4*(1+B[k])
    avg_unique = np.zeros(N, dtype=float)
    rt = np.zeros(N, dtype=float)
    nu = np.zeros(N-2, dtype=float)
    x = np.zeros(N)
    y = np.zeros(N)
    unique = set()
    for j in range(Ns):
        x[0] = 0
        y[0] = 0
        unique.add((x[0],y[0]))
        avg_unique[0] = avg_unique[0]+len(unique)/Ns
        prev_step = 0
        step = random.random()
        if(step<0.25):
            x[1] = -1
            y[1] = 0
            prev_step = 1
        if (0.25<=step<0.5):
            x[1] = 0
            y[1] = -1
            prev_step = 2
        if(0.5<=step<0.75):
            x[1] = 1
            y[1] = 0
            prev_step = 3
        if (0.75<=step):
            x[1] = 0
            y[1] = 1
            prev_step = 4
        rt[1] = rt[1]+(x[1]*x[1]+y[1]*y[1])/Ns
        unique.add((x[1],y[1]))
        avg_unique[1] = avg_unique[1]+len(unique)/Ns
        for i in range(2,N):
            step = random.random()
            if prev_step==1:
                if(step<p_c):
                    x[i] = x[i-1]-1
                    y[i] = y[i-1]
                    prev_step = 1
                if (p_c<=step<p_c+p_a):
                    y[i] = y[i-1]-1
                    x[i] = x[i-1]
                    prev_step = 2
                if(p_c+p_a<=step<p_c+2*p_a):
                    x[i] = x[i-1]+1
                    y[i] = y[i-1]
                    prev_step = 3
                if (p_c+2*p_a<=step):
                    y[i] = y[i-1]+1
                    x[i] = x[i-1]
                    prev_step = 4
            if prev_step==2:
                if(step<p_c):
                    x[i] = x[i-1]-1
                    y[i] = y[i-1]
                    prev_step = 1
                if (p_c<=step<2*p_c):
                    y[i] = y[i-1]-1
                    x[i] = x[i-1]
                    prev_step = 2
                if(2*p_c<=step<2*p_c+p_a):
                    x[i] = x[i-1]+1
                    y[i] = y[i-1]
                    prev_step = 3
                if (2*p_c+p_a<=step):
                    y[i] = y[i-1]+1
                    x[i] = x[i-1]
                    prev_step = 4
            if prev_step==3:
                if(step<p_a):
                    x[i] = x[i-1]-1
                    y[i] = y[i-1]
                    prev_step = 1
                if (p_a<=step<p_a+p_c):
                    y[i] = y[i-1]-1
                    x[i] = x[i-1]
                    prev_step = 2
                if(p_a+p_c<=step<2*p_c+p_a):
                    x[i] = x[i-1]+1
                    y[i] = y[i-1]
                    prev_step = 3
                if (2*p_c+p_a<=step):
                    y[i] = y[i-1]+1
                    x[i] = x[i-1]
                    prev_step = 4
            if prev_step==4:
                if(step<p_a):
                    x[i] = x[i-1]-1
                    y[i] = y[i-1]
                    prev_step = 1
                if (p_a<=step<2*p_a):
                    y[i] = y[i-1]-1
                    x[i] = x[i-1]
                    prev_step = 2
                if(2*p_a<=step<2*p_a+p_c):
                    x[i] = x[i-1]+1
                    y[i] = y[i-1]
                    prev_step = 3
                if (2*p_a+p_c<=step):
                    y[i] = y[i-1]+1
                    x[i] = x[i-1]
                    prev_step = 4
            
            rt[i] = rt[i] + (x[i]*x[i] + y[i]*y[i])/Ns
            unique.add((x[i],y[i]))
            avg_unique[i] = avg_unique[i] + len(unique)/Ns
        unique.clear()
        re[j,k] = m.sqrt(x[-1]*x[-1]+y[-1]*y[-1])
        #print(j)
    for i in range(3,N-1):
        nu[i-3] = m.log(rt[i+1]/rt[i-1])/(2*m.log((i+1)/(i-1)))
    

    
    sns.distplot(re[:,k], bins = 100)
    plt.title('Distribution of Average End to End disatnce for B = ' + str(B[k]))
    plt.xlabel('Average End to End distance')
    plt.ylabel('Frequency')
    plt.show()
    tmp = np.arange(N, dtype=float)
    plt.scatter(x[1:10000],y[1:10000],s=0.5)
    plt.plot(x[1:10000],y[1:10000])
    plt.title('Spiral Random Walk of 10000 Steps for B = ' + str(B[k]))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    plt.plot(tmp,avg_unique)
    plt.title('Number of Sites Visited for B = ' + str(B[k]))
    plt.xlabel('Number of Steps (Time)')
    plt.ylabel('Number of Unique Sites Visited (N_cov)')
    plt.show()
    sum_x = 0
    sum_x2 = 0
    sum_y = 0
    sum_xy = 0
    for i in range(1,N):
        tmp[i] = m.log(tmp[i])
        rt[i] = m.log(rt[i])
        sum_x = sum_x+tmp[i]
        sum_x2 = sum_x2 + tmp[i]*tmp[i]
        sum_y = sum_y+rt[i]
        sum_xy = sum_xy+tmp[i]*rt[i]
    plt.plot(tmp,rt)
    plt.title('Square of Distance Travelled vs Time for B = ' + str(B[k]))
    plt.xlabel('Number of Steps (Time)')
    plt.ylabel('Square of Distance Travelled')
    plt.show()
    nu_fin = ((N*sum_xy-(sum_x*sum_y))/(N*sum_x2-(sum_x*sum_x)))/2
    print('The diffusion constant of the Random walk comes as', nu_fin)
    tmp = np.arange(2,N)
    plt.plot(1/tmp,nu)
    plt.title('Diffusion Coefficient vs 1/Time for B = ' + str(B[k]))
    plt.ylabel('Diffusion Coefficient')
    plt.xlabel('1/Number of Steps (1/Time)')
    plt.show()