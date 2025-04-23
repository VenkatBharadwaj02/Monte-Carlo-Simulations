L = 40:20:160;
P = 0.5:0.002:0.7;
N=10000;
pinf = zeros(length(L),length(P));
csd = zeros(length(L),length(P));
bc = zeros(length(L),length(P));
a = zeros(length(L),length(P));
b = zeros(length(L),length(P));

for n = 1:N
    for l = 1:length(L)
        for p = 1:length(P)
            lat = zeros(L(l),L(l));
            %count=0;
            for i = 1:L(l)
                for j = 1:L(l)
                    r = rand;
                    if r<P(p)
                        lat(i,j) = 1;
                        %count=count+1;
                    end
                end
            end
            %disp(count/(L(l)*L(l)))
            %disp(lat)
            hk = zeros(L(l),L(l));
            mass = [0];
            k=1;
            for i = 1:L(l)
                for j = 1:L(l)
                    if i==1
                        if j==1
                            if lat(i,j)
                                hk(i,j) = k;
                                k=k+1;
                                mass = [mass,0];
                                mass(hk(i,j)) = mass(hk(i,j))+1;
                                continue;
                            else
                                continue;
                            end
                        else
                            if lat(i,j)
                                if lat(i,j-1)
                                    hk(i,j) = hk(i,j-1);
                                    mass(hk(i,j)) = mass(hk(i,j))+1;
                                    continue;
                                else
                                    hk(i,j) = k;
                                    k=k+1;
                                    mass = [mass,0];
                                    mass(hk(i,j)) = mass(hk(i,j))+1;
                                    continue;
                                end
                            end
                        end
                    end
                    if j==1
                        if lat(i,j)
                            if lat(i-1,j)
                                tmp = mass(hk(i-1,j));
                                tmp1= hk(i-1,j);
                                while tmp<0
                                    tmp1 = tmp;
                                    tmp = mass(abs(tmp1));
                                end
                                hk(i,j) = abs(tmp1);
                                mass(hk(i,j)) = mass(hk(i,j))+1;
                                continue;
                            else
                                hk(i,j) = k;
                                k=k+1;
                                mass = [mass,0];
                                mass(hk(i,j)) = mass(hk(i,j))+1;
                                continue;
                            end
                        end
                    end
                    if lat(i,j)
                        if lat(i-1,j)
                            if lat(i,j-1)
                                if hk(i,j-1) == hk (i-1,j)
                                    hk(i,j) = hk(i-1,j);
                                    mass(hk(i,j)) = mass(hk(i,j))+1;
                                    continue;
                                end
                                tmp = mass(hk(i-1,j));
                                tmp1= hk(i-1,j);
                                while tmp<0
                                    tmp1 = tmp;
                                    tmp = mass(abs(tmp1));
                                end
                                tmp = mass(hk(i,j-1));
                                tmp2= hk(i,j-1);
                                while tmp<0
                                    tmp2=tmp;
                                    tmp = mass(abs(tmp2));
                                end
                                if abs(tmp1)==abs(tmp2)
                                    hk(i,j) = abs(tmp1);
                                    mass(hk(i,j)) = mass(hk(i,j))+1;
                                else
                                    hk(i,j) = min(abs(tmp1),abs(tmp2));
                                    mass(hk(i,j)) = mass(abs(tmp1))+mass(abs(tmp2))+1;
                                    mass(max(abs(tmp1),abs(tmp2))) = -1*hk(i,j);
                                end
                            else
                                tmp = mass(hk(i-1,j));
                                tmp1=hk(i-1,j);
                                while tmp<0
                                    tmp1 = tmp;
                                    tmp = mass(abs(tmp1));
                                end
                                hk(i,j) = abs(tmp1);
                                mass(hk(i,j)) = mass(hk(i,j))+1;
                            end
                        elseif lat(i,j-1)
                            tmp = mass(hk(i,j-1));
                            tmp1= hk(i,j-1);
                            while tmp<0
                                tmp1 = tmp;
                                tmp = mass(abs(tmp1));
                            end
                            hk(i,j) = abs(tmp1);
                            mass(hk(i,j)) = mass(hk(i,j))+1;
                        else
                            hk(i,j) = k;
                            k=k+1;
                            mass = [mass,0];
                            mass(hk(i,j)) = mass(hk(i,j))+1;
                        end
                    end
                end
            end
            %disp(hk)
            s = [];
            ns = [];
            for t = 1:length(mass)
                if mass(t)>0
                    if ismember(mass(t),s)
                        continue;
                    else
                        s = [s,mass(t)];
                        bla = 0;
                        for i = 1:length(mass)
                            if mass(i)==mass(t)
                                bla = bla+1;
                            end
                        end
                        ns = [ns,bla];
                    end
                end
            end
            %disp(s)
            %disp(ns)
            perc = [];
            for i = 1:L(l)
                if hk(1,i) ~=0
                    for j = 1:L(l)
                        if hk(L(l),j) == hk(1,i)
                            if ismember(hk(1,i),perc)
                                continue;
                            else
                                perc = [perc,hk(1,i)];
                            end
                        end
                    end
                end
            end    
            %disp(perc)
            massinf = zeros(length(perc),1);
            tmp = 0;
            for i = 1:length(perc)
                massinf(i) = mass(perc(i));
                tmp = tmp+massinf(i)/(L(l)*L(l));
            end
            for i = 1:length(s)
                if ismember(s(i),massinf)
                    continue;
                else
                    %tmp = tmp-s(i)*ns(i)/(L(l)*L(l));
                    csd(l,p) = csd(l,p)+s(i)*s(i)*ns(i)/(L(l)*L(l));
                end
            end
            pinf(l,p) = tmp+pinf(l,p);
            a(l,p) = a(l,p)+(tmp)^4;
            b(l,p) = b(l,p)+(tmp)^2;
        end
    end
    disp(n)
end
pinf = pinf/N;
csd = csd/N;
a = a;
b = b;
for l = 1:length(L)
    for p = 1:length(P)
        bc(l,p) = (1-(a(l,p)/(3*b(l,p)^2)));
    end
end
%disp(pinf1)
figure(1);
title('Order Parameter (P_{inf}) vs Occupation Probability (p) for various Lattice size')
xlabel('p')
ylabel('P_{inf}')
hold on;
for i = 1:length(L)
    plot(P,pinf(i,:))
end
legend({'L = 40','L = 60','L = 80','L = 100','L = 120','L = 140','L = 160'})
hold off;

figure(2);
title('Average Cluster Size (Chi) vs Ocupation Probability (p) for various Lattice size')
xlabel('p')
ylabel('Chi')
hold on;
for i = 1:length(L)
    plot(P,csd(i,:))
end
legend({'L = 40','L = 60','L = 80','L = 100','L = 120','L = 140','L = 160'})
hold off;

figure(3);
hold on;
title('Binder Cumulant (U) vs Occupation Probability (p) for various Lattice size')
xlabel('p')
ylabel('U')
for i = 1:length(L)
    plot(P,bc(i,:))
end
legend({'L = 40','L = 60','L = 80','L = 100','L = 120','L = 140','L = 160'})
hold off;

writematrix(pinf, 'Pinf.csv')
writematrix(csd, 'csd.csv')
writematrix(bc, 'bc.csv')