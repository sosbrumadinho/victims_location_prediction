function [Reg] = Converte_Regioes_em_Utm(regi)

    R = regi;

    for r = 1:1:length(regi)

        [x, y] = deg2utm(regi(r,2), regi(r,1));
        R(r, 1) = x;
        R(r, 2) = y;
        [x, y] = deg2utm(regi(r,4), regi(r,3));
        R(r, 3) = x;
        R(r, 4) = y;
        
    end
    Reg = R;
    
end