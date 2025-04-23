Tc = 2/(log(1+sqrt(2)));
L = 128;
Temp = 1.25:0.05:3.25;
lat = rand(L,L);
p=0.5;
lat = sign(lat);
e = zeros(L,L);
tmax = 50000;
E = zeros(tmax,1);
mag = zeros(tmax,1);
E2avg = zeros(length(Temp),1);
Eavg = zeros(length(Temp),1);
mavg = zeros(length(Temp),1);
m2avg = zeros(length(Temp),1);
sus = zeros(length(Temp),1);
sh = zeros(length(Temp),1);
for k = 1:length(Temp)
    count = 0;
    t = 0;
    while t < tmax
        for i = 1:L
            for j = 1:L
                e(i,j) = -lat(i,j)*(lat(mod(i-2,L)+1,j)+lat(i,mod(j-2,L)+1)+lat(mod(i,L)+1,j)+lat(i,mod(j,L)+1));
                dE = -2*e(i,j);
                p = exp(-dE/Temp(k));
                r = rand();
                if r <= p
                    lat(i,j) = -lat(i,j);
                end
            end
        end
        
        mag(t+1) = abs(sum(sum(lat))/(L*L));
        E(t+1) = sum(sum(e))/2;
        if t > 1000 && mod(t,100) == 0
            count = count + 1;
            Eavg(k) = Eavg(k) + E(t+1); 
            mavg(k) = mavg(k) + mag(t+1);
            E2avg(k) = E2avg(k) + E(t+1)*E(t+1);
            m2avg(k) = m2avg(k) + mag(t+1)*mag(t+1);
        end
        %disp(t);
        t = t + 1;
    end
    % figure;
    % plot(0:tmax-1,mag);
    % title('Magnetization');
    % xlabel('Time');
    % ylabel('Magnetization');
    % figure;
    % plot(0:tmax-1,E);     
    % title('Energy');
    % xlabel('Time');
    % ylabel('Energy');
    % figure;
    % imagesc(lat);
    % title('Lattice');
    disp(Temp(k))
end
Eavg = Eavg/count;
mavg = mavg/count;
m2avg = m2avg/count;
E2avg = E2avg/count;
for i = 1:length(Temp)
    sus(i) = L*L*(m2avg(i) - mavg(i)*mavg(i))/(Temp(i));
    sh(i) = (E2avg(i) - Eavg(i)*Eavg(i))/(Temp(i)*Temp(i));
end

figure;
plot(Temp,mavg);
figure;
plot(Temp,Eavg/(L*L));
figure;
plot(Temp,sus);
figure;
plot(Temp,sh);

writematrix([mavg Eavg sh sus], 'data.csv')

