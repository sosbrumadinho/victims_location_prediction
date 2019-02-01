function [utm] = MDTgradient(data,step)
% Computes module and angle of MDT in matrix form
% Inputs:
%   data: matrix elements in the form {[lat,long,alt]} with lat,long in the
%   UTM system
%   step: step between elements [m]
% Outputs:
%   utm: xy projections final positions in the UTM system
    
    [r,c] = size(data);
    utm = repmat({[0,0]},r,c);
    for i_r = 2:r-1
        for i_c = 2:c-1
            cell_a = cell2mat(data(i_r-1,i_c-1));
            cell_b = cell2mat(data(i_r-1,i_c));
            cell_c = cell2mat(data(i_r-1,i_c+1));
            cell_d = cell2mat(data(i_r,i_c-1));
            cell_e = cell2mat(data(i_r,i_c));
            cell_f = cell2mat(data(i_r,i_c+1));
            cell_g = cell2mat(data(i_r+1,i_c-1));
            cell_h = cell2mat(data(i_r+1,i_c));
            cell_i = cell2mat(data(i_r+1,i_c+1));
            a = cell_a(3);
            b = cell_b(3);
            c = cell_c(3);
            d = cell_d(3);
            f = cell_f(3);
            g = cell_g(3);
            h = cell_h(3);
            i = cell_i(3);
            dz_dx = ((a+2*d+g)-(c+2*f+i))/(8*step);
            dz_dy = ((g+2*h+i)-(a+2*b+c))/(8*step);
            dh_dp = sqrt((dz_dx)^2+(dz_dy)^2);
            mod = dh_dp;
            ang = rad2deg(atan(dz_dx/dz_dy))+180;
            utm(i_r,i_c) = {[cell_e(1)+mod*step*cosd(ang),...
                cell_e(2)+mod*step*sind(ang)]};
        end
    end
end