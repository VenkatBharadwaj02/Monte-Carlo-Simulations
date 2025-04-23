R = 1+rand;
L = 20*R;
R
Nmax = floor(L^3*0.74*3/(4*pi*R^3));
M = 10000;
N = zeros(M,1);
rmean = zeros(M,1);

for i = 1:M
    accept = 1;
    reject = 0;
    spheres = [[R+(L-2*R)*rand R+(L-2*R)*rand R+(L-2*R)*rand]];
    while(reject<10*Nmax)
        tmp=0;
        rm=0;
        x1 = R+(L-2*R)*rand;
        y1 = R+(L-2*R)*rand;
        z1 = R+(L-2*R)*rand;
        for j = 1:accept
            r = sqrt((x1-spheres(j,1))^2+(y1-spheres(j,2))^2+(z1-spheres(j,3))^2);
            if(r>=2*R)
                rm=rm+r;
            else
                tmp=1;
                break
            end
        end
        if tmp==0
            reject=0;
            accept=accept+1;
            rmean(i) = rmean(i)+rm;
            spheres(accept,1) = x1;
            spheres(accept,2) = y1;
            spheres(accept,3) = z1;
        else
            reject=reject+1;
        end
    end
    N(i) = accept;
    rmean(i) = 2*rmean(i)/(N(i)*(N(i)-1));
end

figure(4)
hold on;
[x, y, z] = sphere;
x = x*R;
y = y*R;
z = z*R;
light              
lighting gouraud

plot3([0, L],[0, 0],[0, 0], 'k');
plot3([0, L],[L, L],[0, 0], 'k');
plot3([0, L],[0, 0],[L, L], 'k');
plot3([0, L],[L, L],[L, L], 'k');
plot3([0, 0],[0, L],[0, 0], 'k');
plot3([L, L],[0, L],[0, 0], 'k');
plot3([0, 0],[0, L],[L, L], 'k');
plot3([L, L],[0, L],[L, L], 'k');
plot3([0, 0],[0, 0],[0, L], 'k');
plot3([L, L],[L, L],[0, L], 'k');
plot3([0, 0],[L, L],[0, L], 'k');
plot3([L, L],[0, 0],[0, L], 'k');
xlabel('x');
ylabel('y');
zlabel('z');


for count = 1:accept
    surf(x+spheres(count,1), y+spheres(count,2), z+spheres(count,3),'EdgeColor','none','Facecolor','r')
end
annotation('textbox',[0.6, 0.85, 0.1, 0.1] ,'String', "L = " + L + "; r = " + R)

view([30,30])

writematrix([N rmean], 'Data1.csv')


