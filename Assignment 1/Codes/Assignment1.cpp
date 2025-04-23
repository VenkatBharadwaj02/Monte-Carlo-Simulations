#include <bits/stdc++.h>
#include <random>

using namespace std;

double random()
{
    random_device rd;
    mt19937 generator(rd());
    uniform_real_distribution<double> u(0.0, 1.0);
    return u(generator);
}

int main()
{
    double R=1+random();
    double L = 20*R;
    int Nmax = pow(L,3)*0.74*3/(4*3.14*pow(R,3));
    int M = 100;
    vector<int> N(M);
    vector<double> rmean(M);

    for(int i=0; i<M; i++)
    {
        int accept=0;
        int reject=0;
        vector<vector<double>> spheres{{R + (L-2*R)*random(),R + (L-2*R)*random(),R + (L-2*R)*random()}};
        while (reject<10*Nmax)
        {
            int tmp=0;
            double rm=0;
            double x1 = R + (L-2*R)*random();
            double y1 = R + (L-2*R)*random();
            double z1 = R + (L-2*R)*random();
            for(int j=0; j<spheres.size(); j++)
            {
                double r = sqrt(pow((x1-spheres[j][0]),2)+pow((y1-spheres[j][1]),2)+pow((z1-spheres[j][2]),2));
                if(r>=2*R)
                {
                    rm = rm+r;
                }
                else
                {
                    tmp=1;
                    break;
                }
            }
            if(tmp==1)
            {
                reject++;
            }
            else
            {
                reject=0;
                accept++;
                rmean[i] = rmean[i]+rm;
                spheres.push_back({x1,y1,z1});

            }
        }
        N[i] = accept;
        rmean[i] = 2*rmean[i]/(N[i]*(N[i]-1));
        cout << i << endl;
    }
    return 0;
}

