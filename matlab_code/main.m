%C�DIGO PARA OBTEN��O DA POSI��O DE V�TIMAS EM BRUMADINHO
%Em desenvolvimento por: Rafael Pinheiro, Bruno Turrim 
%                        Isabella Stevani
%                        Lab. de Automa��o e Controle, Engenharia El�trica, Poli-USP.
%                        
%                        
%                        
%Data: 02/02/2019


close all;
clear all;

%POSI��O INICIAL - TRANSFORMA DE COORD. GEOGR�FICAS PARA COORD. UTM

Lat =-20.125859 %Posi��o inicial da v�tima
Lon =-44.120107 %Posi��o inicial da v�tima
[x0,y0,utmzone] = deg2utm(Lat,Lon); 

M = 80; %Massa da v�tima


UTM_da_Regiao_Toda;
Criar_Reg;  %Cria as regi�es
Plotar_Campo_de_Velocidades; %futuramente usar MDTgradient.m


%****************************************************
%INTEGRA A ACELERA��O (ORIGINADA DA FOR�A DE ARRASTO) E OBTEM A VELOCIDADE
%****************************************************


% achar a regi�o inicial
r0 = find((Reg(1:end, 1) <= x0 & Reg(1:end, 3) > x0) ...
         &(Reg(1:end, 2) >= y0 & Reg(1:end, 4) < y0), 1);

% Velocidade do fluido na regi�o inicial
[Vx0, Vy0] = Campo_Velocidades(Reg(r0:r0,9), x0, y0, Reg);
[ax0_rej, ay0_rej] = Forca_de_Arraste1([Vx0, Vy0]);
ax0_rej = ax0_rej/M; 
ay0_rej = ay0_rej/M;

Ult_Reg = int16(20*r0/Reg(r0:r0,9));

a_rej_x = zeros(Ult_Reg, 1);
a_rej_y = zeros(Ult_Reg, 1);
regioes = zeros(Ult_Reg, 1);

a_rej_x(1) = ax0_rej;
a_rej_y(1) = ay0_rej;
regioes(1) = r0;

t = Reg(r0:r0,9);

atual = r0;
for r = 2:Ult_Reg   
    proximo = Reg(atual, 6);
    regioes(r) = proximo;
    t = t + Reg(atual:atual,9);
    x = (Reg(proximo, 3) - Reg(proximo, 1))/2 + Reg(proximo, 1);
    y = (Reg(proximo, 4) - Reg(proximo, 2))/2 + Reg(proximo, 2);
    [Vx, Vy] = Campo_Velocidades(t, x, y, Reg);
    [ax, ay] = Forca_de_Arraste1([Vx, Vy]);
    a_rej_x(r) = ax/M;
    a_rej_y(r) = ay/M;
    atual = proximo;
end

a_cp_x = a_rej_x;
a_cp_y = a_rej_y;

%INTEGRA NA DIRE��O X - OBTEM A VELOCIDADE
velx = cumtrapz(a_cp_x);

%INTEGRA NA DIRE��O X - OBTEM A VELOCIDADE
vely = cumtrapz(a_cp_y);

display([velx, vely]);

%******************************************************
%INTEGRA A VELOCIDADE E OBTEM A POSI��O 
%******************************************************

%INTEGRA NA DIRE��O X
cdistanceX = cumtrapz(velx);

%INTEGRA NA DIRE��O Y
cdistanceY = cumtrapz(vely);

%INSERE A POSI��O INICIAL E OBTEM A POSI��O FINAL
cdistanceX(1)=x0;
cdistanceY(1)=y0;
for i=2:Ult_Reg
    cdistanceX(i)=cdistanceX(i)+cdistanceX(i-1);
    cdistanceY(i)=cdistanceY(i)+cdistanceY(i-1);
end


%LATITUDE E LONGITUDE FINAL DA V�TIMA 
[Lat, Lon] = utm2deg(cdistanceX(Ult_Reg),cdistanceY(Ult_Reg),utmzone)

