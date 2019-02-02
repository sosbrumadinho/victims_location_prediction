%% Força de Arrasto
%   Calcula a força de arraste em função da velocidade do fluido
function [Fx, Fy] = Forca_de_Arraste1(V)

    sinal = sign(V);

    den=100;%1000; %a densidade segundo literatura pode variar de 1450 à 2240
    cd=0.05;%0.0001;%1.5;%0.000001; %coeficiente de arrasto estimamos que pode variar de 1.1 à 1.5
    A=1;
    Fx = sinal(1)*0.5*cd*den*V(1)^2*A;
    Fy = sinal(2)*0.5*cd*den*V(2)^2*A;

end