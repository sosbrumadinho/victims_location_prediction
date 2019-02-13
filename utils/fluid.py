import math
import numpy as np
import pandas as pd
import utm


class FLUID():
    """
    For a given region FLUID construct the velocity field and the force field
    """
    _density = 100  # According to the literature, it can vary from 1450 to 2240
    _driftCoef = 0.05  # It expected to be between 1.1 to 1.5
    _A = 1
    _velocityField = pd.DataFrame(columns=['vLon', 'vLat'])
    _forceField = pd.DataFrame(columns=['fLon', 'fLat'])

    def MaxVelocity(self, time):
        "Gives the fluid velocity for a certain time"
        vAux = 10 - (time / 3600.) * 0.137
        return (0 if vAux < 0 else vAux)

    def VelocityAt(self, region):
        # time = region['time']
        # vMax = self.MaxVelocity(time)
        # region = GEOMAP.FindPoint(lon, lat)
        V = region['time'].apply(
            lambda cell: self.MaxVelocity(cell)) * region['E']
        self._velocityField['vLon'] = V * region['centreLonVersor']
        self._velocityField['vLat'] = V * region['centreLatVersor']
        return (self._velocityField)

    def DriftForce(self):
        vLat = self._velocityField['vLat']
        vLon = self._velocityField['vLon']
        vLatSign = vLat.copy()
        vLatSign[vLat >= 0] = 1
        vLatSign[vLat < 0] = -1
        vLonSign = vLon.copy()
        vLonSign[vLon >= 0] = 1
        vLonSign[vLon < 0] = -1
        self._forceField['fLat'] = vLatSign * \
            self._density * self._driftCoef * vLat ** 2 * self._A
        self._forceField['fLon'] = vLonSign * \
            self._density * self._driftCoef * vLon ** 2 * self._A
        return(self._forceField)
