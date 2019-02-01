import numpy as np
import pandas as pd
from utils.vector_field import *

dataSet = np.random.random((9,3))

multiIdx = [[0,1,2], ['lat', 'lon', 'height']]
idxs = pd.MultiIndex.from_product(multiIdx, names=['row', 'geoCoor'])
dataMultiIndex = pd.DataFrame(dataSet, index=idxs)

utmArr = MDTGradient(dataMultiIndex,30)
print(utmArr)