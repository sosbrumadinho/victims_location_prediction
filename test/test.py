import numpy as np
import pandas as pd
from utils.vector_field import *
import utm 
from geomap import MAP
import matplotlib.pyplot as pl
from fluid import FLUID


# Example: 
lat, lon = -20., -44.
x0, y0, utmZoneNumber, utmZoneLetter = utm.from_latlon(lat, lon)
x0, y0 = 590000., 7773100.
# Victm's mass
m = 80 # kg

FluidObj = FLUID()

dataMap = MAP()
dataMap.CentrePoint()
dataSet = dataMap.Data()
# dataSet = np.random.random((9,3))

# multiIdx = [[0,1,2], ['lat', 'lon', 'height']]
# idxs = pd.MultiIndex.from_product(multiIdx, names=['row', 'geoCoor'])
# dataMultiIndex = pd.DataFrame(dataSet, index=idxs)

# utmArr = MDTGradient(dataMultiIndex,30)
# print(utmArr)

# Loads borders of the region 
borders = pd.read_csv('./data/borders.csv')
# converts borders to utm and append it to original borders
borders[ ['x0', 'y0', 'utmZoneNumber', 'utmZoneLetter'] ] = borders.apply( 
    lambda row: pd.Series( 
    list( utm.from_latlon( row['lat'], row['lon'] ) )
    ),
    axis = 1 
)

#####################################

# dataSet = dataMap.Data()

# Plot velocity field: v_vec = vel_u + vel_v
# u = 
dataSet['vel_u'] = dataSet['E'] * dataSet['G']
dataSet['vel_v'] = dataSet['E'] * dataSet['H']

fig = pl.figure(1, figsize = (20, 12))
pl.quiver(
    dataSet['upperLeftLon'], 
    dataSet['upperLeftLat'], 
    dataSet['vel_u'], 
    dataSet['vel_v']
)

# Velocity field
ro = dataMap.FindPoint(x0, y0)
veloc = FluidObj.VelocityAt(ro, 1,  x0, y0)
force = FluidObj.DriftForce()

