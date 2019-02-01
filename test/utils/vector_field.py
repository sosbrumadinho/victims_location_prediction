""" 
Translated from Matlab code.
"""
import math 
import numpy as np

def MDTGradient(data, step):
    """
    Computes module and angle of MDT in a DataFrame multindex form
    Ex.:
                        0         1         2
    row geoCoor
    0   lat      0.798883  0.506124  0.869507
        lon      0.723973  0.835690  0.922523
        height   0.139599  0.127564  0.240762
    1   lat      0.432731  0.385345  0.086345
        lon      0.863745  0.870077  0.754997
        height   0.660120  0.393816  0.488428

    Inputs:
        data: dataframe elements in the form with lat,long in the
        UTM system
        step: step between elements m
    Outputs:
        utm: xy projections final positions in the UTM system
    """
    rows, cols = len(data.index.levels[0]), len(data.columns)
    heights = data.xs('height', level='geoCoor')

    utmXYProj = np.zeros((rows, cols, 2))

    for row in range(1,rows-1):
        for col in range(1,cols-1):
            lat = data.loc[(row, 'lat'), col]
            lon = data.loc[(row, 'lon'), col]

            a = heights.loc[ row-1, col-1 ]
            b = heights.loc[ row-1, col ]
            c = heights.loc[ row-1, col+1 ]
            d = heights.loc[ row, col-1 ]
            f = heights.loc[ row, col+1 ]
            g = heights.loc[ row+1, col-1 ]
            h = heights.loc[ row+1, col ] 
            i = heights.loc[ row+1, col+1 ]

            dz_dx = ((a+2*d+g)-(c+2*f+i))/(8*step)
            dz_dy = ((g+2*h+i)-(a+2*b+c))/(8*step)
            dh_dp = np.sqrt( dz_dx**2 + dz_dy**2)

            mod = dh_dp
            ang = math.atan(dz_dx/dz_dy) + math.pi
            # kept the angle in rads 

            utmXYProj [row , col] = [
                lat + mod * step * math.cos(ang), 
                lon + mod * step * math.sin(ang)
            ]
            return( utmXYProj )

# from matlab:
    # [r,c] = size(data);
    # utm = repmat({[0,0]},r,c);
    # for i_r = 2:r-1
    #     for i_c = 2:c-1
    #         cell_a = cell2mat(data(i_r-1,i_c-1));
    #         cell_b = cell2mat(data(i_r-1,i_c));
    #         cell_c = cell2mat(data(i_r-1,i_c+1));
    #         cell_d = cell2mat(data(i_r,i_c-1));
    #         cell_e = cell2mat(data(i_r,i_c));
    #         cell_f = cell2mat(data(i_r,i_c+1));
    #         cell_g = cell2mat(data(i_r+1,i_c-1));
    #         cell_h = cell2mat(data(i_r+1,i_c));
    #         cell_i = cell2mat(data(i_r+1,i_c+1));
    #         a = cell_a(3);
    #         b = cell_b(3);
    #         c = cell_c(3);
    #         d = cell_d(3);
    #         f = cell_f(3);
    #         g = cell_g(3);
    #         h = cell_h(3);
    #         i = cell_i(3);
    #         dz_dx = ((a+2*d+g)-(c+2*f+i))/(8*step);
    #         dz_dy = ((g+2*h+i)-(a+2*b+c))/(8*step);
    #         dh_dp = sqrt((dz_dx)^2+(dz_dy)^2);
    #         mod = dh_dp;
    #         ang = rad2deg(atan(dz_dx/dz_dy))+180;
    #         utm(i_r,i_c) = {[cell_e(1)+mod*step*cosd(ang),...
    #             cell_e(2)+mod*step*sind(ang)]};

