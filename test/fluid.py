import math 
import numpy as np
import pandas as pd
import utm

class FLUID():
  """
  FLUID object
  """
  _density = 100 # According to the literature, it can vary from 1450 to 2240
  _driftCoef = 0.05 # It expected to be between 1.1 to 1.5
  _A = 1
  _velocityField = pd.DataFrame({'vLon': [0], 'vLat': [0]})
  _forceField = pd.DataFrame({'fLon': [0], 'fLat': [0]})

  def MaxVelocity(self, time):
    "Gives the fluid velocity for a certain time"
    vAux = 10 - (time / 3600.) * 0.137
    return ( 0 if vAux < 0 else vAux )
  
  def VelocityAt (self, region, time, lon, lat):
    vMax = self.MaxVelocity(time)
    # region = GEOMAP.FindPoint(lon, lat)
    V = vMax * region['E'].iloc[0]
    self._velocityField['vLon'] = V * region['centreLonVersor'].iloc[0]
    self._velocityField ['vLat'] = V * region['centreLatVersor'].iloc[0]
    return ( self._velocityField )

  def DriftForce(self):
    vLat = self._velocityField ['vLat'].iloc[0]
    vLon = self._velocityField ['vLon'].iloc[0]

    sign = [vLat/vLat, vLon/vLon]
    self._forceField ['fLat'] = sign[0] * self._density * self._driftCoef * vLat ** 2 * self._A
    self._forceField ['fLon'] = sign[1] * self._density * self._driftCoef * vLon ** 2 * self._A
    return(self._forceField )

    