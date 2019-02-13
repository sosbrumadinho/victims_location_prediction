function [vx, vy] = Campo_Velocidades(t, x, y, Reg)
    
    %m�xima velocidade a cada instante de tempo
    v_max = Velocidade_maxima(t);
    
    % qual a regi�o � qual aquele ponto pertence
    reg = Achar_Regiao(Reg, [x, y]);
    
    % existe velocidade nessa regi�o
    V = v_max*Reg(reg, 5);
    
    if V ~= 0
        ap = Reg(reg, 6);
        [p1x, p1y] = Ponto_central([Reg(reg,1), Reg(reg,2)], ...
                                   [Reg(reg,3), Reg(reg, 4)]);
        [p2x, p2y] = Ponto_central([Reg(ap,1), Reg(ap,2)], ...
                                   [Reg(ap,3), Reg(ap, 4)]);
                       
        [i, j] = Versor([p1x, p1y], [p2x, p2y]);
        
        vx = i*V;
        vy = j*V;
    else
        vx = 0;
        vy = 0;
    end
end


%%
% Estimativa da velocidade do rejeito no tempo
function [v] = Velocidade_maxima(t)
    
    v_aux = 10 -(t/3600)*0.137;
    if v_aux<0
        v_aux = 0;
    end 
    
    v = v_aux;    
end


%%
% Calcula o ponto central de uma regi�o
function [x, y] = Ponto_central(p1, p2)

    x = (p2(1)-p1(1))/2 + p1(1);
    y = (p2(2)-p1(2))/2 + p1(2);

end

%%
% Acha a regi�o em que a posi��o se encaixa
function [r] = Achar_Regiao(reg, posicao)
    r = find((reg(1:end, 1) <= posicao(1) & reg(1:end, 3) > posicao(1)) ...
            &(reg(1:end, 2) >= posicao(2) & reg(1:end, 4) < posicao(2)), 1);
end

%%
% Calcula o Versor de uma regi�o
function [i, j] = Versor(p1, p2)

    Vx = p2(1) - p1(1);
    Vy = p2(2) - p1(2);
    M = sqrt(Vx^2 + Vy^2);
    
    i = Vx/M;
    j = Vy/M;
end