import math
import numpy as np
import pandas as pd
import utm


class MAP():
    """
    MAP loads data from a csv file (region.csv) placed in the data folder
    """
    _data = {}
    _fileName = './data/region.csv'

    def __init__(self):
        # loading data
        self._data = pd.read_csv(self._fileName)
        print('Data successfully loaded!')

    def Data(self):
        "Returns raw data"
        return(self._data)

    def CentrePoint(self):
        "Returns the point at the centre of the square and its versor"

        vX = self._data['upperLeftLat'] - self._data['lowerRightLat']
        vY = self._data['lowerRightLon'] - self._data['upperLeftLon']
        m = (vX ** 2 + vY ** 2) ** 0.5

        self._data['centreLat'] = vX / 2 + self._data['upperLeftLat']
        self._data['centreLon'] = vY / 2 + self._data['lowerRightLon']

        self._data['centreLatVersor'] = vX / m
        self._data['centreLonVersor'] = vY / m

        return(
          self._data[['centreLon', 'centreLat']],
          self._data[['centreLonVersor', 'centreLatVersor']]
        )

    def FindPoint(self, lon, lat):
        """
          Finds the closest location on the map relative
          to the given point (lon, lat) in utm format
        """
        condition = (
          (self._data['upperLeftLat'] >= lat) &
          (lat > self._data['lowerRightLat']) &
          (self._data['upperLeftLon'] < lon) &
          (lon <= self._data['lowerRightLon'])
        )
        return (self._data[condition])

    def MdtGradient(self, data, step):
        """
        NOT being used. It has to be modified to be included in the main code
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

        for row in range(1, rows-1):
            for col in range(1, cols-1):
                lat = data.loc[(row, 'lat'), col]
                lon = data.loc[(row, 'lon'), col]

                a = heights.loc[row-1, col-1]
                b = heights.loc[row-1, col]
                c = heights.loc[row-1, col+1]
                d = heights.loc[row, col-1]
                f = heights.loc[row, col+1]
                g = heights.loc[row+1, col-1]
                h = heights.loc[row+1, col]
                i = heights.loc[row+1, col+1]

                dz_dx = ((a+2*d+g)-(c+2*f+i))/(8*step)
                dz_dy = ((g+2*h+i)-(a+2*b+c))/(8*step)
                dh_dp = np.sqrt(dz_dx**2 + dz_dy**2)

                mod = dh_dp
                ang = math.atan(dz_dx/dz_dy) + math.pi
                # kept the angle in rads

                utmXYProj[row, col] = [
                    lat + mod * step * math.cos(ang),
                    lon + mod * step * math.sin(ang)
                ]
                return(utmXYProj)
