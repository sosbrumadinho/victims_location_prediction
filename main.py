"""
Modeling to estimate the victims' positions in Brumadinho
Underdevelopment: 
    Rafael Pinheiro*, Bruno Turrim*
    Alexandre Rodrigues*, Isabela Stevani*
    Andre, Marconi*, Leonardo Carvalho*
    *Lab de Automacao e Controle, Electric Engineering, Poli-USP - SP Brazil

    Thamires Chagas**
    **ITA, Brazil

    Jean Matias***
    ***Tyndall National Institute, UCC - Cork, Ireland
"""
import numpy as np
import pandas as pd
import utm
from scipy.integrate import cumtrapz
import matplotlib.pyplot as pl
from utils.geomap import MAP
from utils.fluid import FLUID

# Example:
# Initial position
lat, lon = -20.137228709820736, -44.13889842358328
# The above values are outside the region, then it gives an error
# Thus, I used x0 and y0 inputted manually
x0, y0, utmZoneNumber, utmZoneLetter = utm.from_latlon(lat, lon)
x0, y0 = 590010., 7773100.  # <------ manually
# Victim's mass
m = 80  # kg

# Loads fluid class
FluidObj = FLUID()
# Loads map class
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
borders[['x0', 'y0', 'utmZoneNumber', 'utmZoneLetter']] = borders.apply(
    lambda row: pd.Series(
        list(utm.from_latlon(row['lat'], row['lon']))
    ),
    axis=1
)

#####################################
# Plot velocity field: v_vec = vel_u + vel_v
dataSet['vel_u'] = dataSet['E'] * dataSet['G']
dataSet['vel_v'] = dataSet['E'] * dataSet['H']

fig, ax = pl.subplots(1, figsize=(15, 9))
q = ax.quiver(
    dataSet['upperLeftLon'],
    dataSet['upperLeftLat'],
    dataSet['vel_u']/2,
    dataSet['vel_v']/2,
    scale=32,
)
pl.show()

# Fluid element properties

# Finds the initial position on the map
ro = dataMap.FindPoint(x0, y0)
lastRegion = int(20 * ro.index[0] / ro['time'].iloc[0])
idx = ro.index[0]
fluidElems = dataSet.iloc[idx: idx + lastRegion]
fluidElems[['vLon', 'vLat']] = FluidObj.VelocityAt(fluidElems)
fluidElems[['fLon', 'fLat']] = FluidObj.DriftForce()

# Acceleration Field
accelerationX = fluidElems['fLon'] / m
accelerationY = fluidElems['fLat'] / m

# Converting to numpy array to fit to what is already done
accelerationX = np.array(accelerationX)
accelerationY = np.array(accelerationY)
# time = 24 #seconds or min?

# Integrate on the x direction
velocityX = cumtrapz(accelerationX)
# Integrate on the x direction
velocityY = cumtrapz(accelerationY)

# Integrate velocity to get x position
positionX = cumtrapz(velocityX)
# Integrate velocity to get y position
positionY = cumtrapz(velocityY)

# Insert initial position
positionX = np.concatenate([[x0], positionX])
positionY = np.concatenate([[y0], positionY])

# Using cumulative sum instead of for
positionX = np.cumsum(positionX)
positionY = np.cumsum(positionY)

# Gets latitude and longitude of an object in the fluid waste
lat, lon = utm.to_latlon(
    positionX[-1], positionY[-1], utmZoneNumber, utmZoneLetter)

print(
    '''Final position:
        lat: %f
        lon: %f
    ''' % (lat, lon)
)
