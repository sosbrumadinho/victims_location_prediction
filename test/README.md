# Vectorial field calculation

Initial stage of the vectorial field calculation

## ToDO list

### Translate the following MATLAB codes:
- [ ]  [main](../matlab_code/main.m): Calls all the functions (main script)  
    **Translation**: Partially translated
- [ ]  [Forca_de_Arraste1](../matlab_code/Forca_de_Arraste1.m): Calculated the drift force as a function of the fluid speed  

- [ ]  [Campo_Velocidades](../matlab_code/Campo_Velocidades.m): Returns the fluid vectorial velocity (`vx, vy`) for a given time and position on the map (`t, x, y, Reg`)  

- [ ]  [Plotar_Campo_de_Velocidades](../matlab_code/Plotar_Campo_de_Velocidades.m): Plots the vectorial velocity field

- [ ]  [UTM_da_Regiao_Toda](../matlab_code/UTM_da_Regiao_Toda.m): It still not clear what this part of the code does. 

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
