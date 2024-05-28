#import reflex as rx
import pandas as pd
#import openpyxl
import math

#ruta= r'C:\Users\jovid\Documents\015 JOSE\070 ENERGIA\00001 PUBLICACIONES LINKEDIN\002 Miniporras\SUPERPORRA2024.xlsm'
ruta= 'SUPERPORRA2024.xlsm'
datos=pd.read_excel(ruta,sheet_name='acum_porc')
#datos=datos.iloc[:,9]
datos=datos[['Clasificación', '%_desvio']]
datos=datos.to_dict(orient='records')
datos = [dato for dato in datos if not math.isnan(dato['%_desvio'])]
for registro in datos:
    registro["%_desvio"] = "{:.3f}".format(registro["%_desvio"])

