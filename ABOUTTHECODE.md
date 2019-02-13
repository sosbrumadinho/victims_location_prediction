# Position Modeling


The main.py file calls the classes inside the utils folder. The script tries to estimate the position of the victims or animals drifted by the mud. 
This approach aims to construct a vectorial field of the mud's drift force running off down the valley. 

From this force vectorial field, it is possible to calculate the acceleration vectorial field and after integration processes possible final positions of the bodies can be estimated considering their initial position. 

One of the possible ways to get the initial position is from GPS geolocation of the victims' cell phones at the time of the Dam burst. 

# The code

The original code was written in MATLAB and then translated to Python. 

The [main.py](./main.py) file gets the geolocation coordinates and converts to x and y positions, which are used as boundary conditions. Data in the data folder are used to delimit the region affected by the accident. This region is passed to the FLUID class which calculates the velocity field and force field. As consequence, using an average mass equals 80kg, the acceleration field is obtained.  
After two integrations of the acceleration field, the code calculates the positions of the body. The final position is then determined using the last value in the position array. 

To start simply run from a Python interactive terminal:
```
run main
```
---
## Details of the MATLAB code translation to Python:
- [x]  [main](../matlab_code/main.m): Calls all the functions (main script)  
    **Translation**: [main.py](./main.py)    
- [x]  [Forca_de_Arraste1](../matlab_code/Forca_de_Arraste1.m): Calculates the drift force as a function of the fluid speed  
    **Translation**: Included to FLUID class

- [x]  [Campo_Velocidades](../matlab_code/Campo_Velocidades.m): Returns the fluid vectorial velocity (`vx, vy`) for a given time and position on the map (`t, x, y, Reg`)  
    **Translation**: Included to FLUID class

- [x]  [Plotar_Campo_de_Velocidades](../matlab_code/Plotar_Campo_de_Velocidades.m): Plots the vectorial velocity field
    **Translation**: Used a matplotlib in the main file

- [x]  [UTM_da_Regiao_Toda](../matlab_code/UTM_da_Regiao_Toda.m): Borders of the region is stored at [border.csv](./data/borders.csv) 

- [x]  [Criar_Reg](../matlab_code/Criar_Reg.m): Generate the initial data to be used during the analysis  
    **Translation**: csv file [region.csv](./data/region.csv)

- [x]  [Converte_Regions_em_Utm](../matlab_code/Converte_Regions_em_Utm.m): Converts geo-coordinates from degrees to utm format for the whole map (`regi`)  
    **Translation**: [MAP.Utm( )](./map.py) => Used `utm.from_latlon()` method applied to a pandas DataFrame by the `pd.apply( )` method. 
    
- [x]  [deg2utm](../matlab_code/deg2utm.m): Converts geo-coordinates from degree to utm format  
    **Translation**: Using a external module: `utm` 
- [x]  [utm2deg](../matlab_code/utm2deg.m)  
    **Translation**: Using a external module: `utm` 

- [x]  [MDTgradient](../matlab_code/MDTgradient.m): Computes module and angle of MDT in matrix form. It is based on the Descendent Gradient algorithm  
    **Translation**: [MAP.MdtGradient( )](./map.py) **Partially solved**. It has to be modified to match with the current data in the csv file.

All the functions related to the mao were translated to methods in the [MAP](./map.py) class.
