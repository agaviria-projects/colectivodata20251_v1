import pandas as pd

#Leyendo los datos de asistencias
asistenciaDataFrame=pd.read_csv("../data/asistencia_estudiantes_completo.csv")
#print(asistenciaDataFrame)

#Obteniendo informacion basica del dataframe
#print(asistenciaDataFrame.info())

#Obtener los primeros 20 registros
#print(asistenciaDataFrame.head(20))

#Obtener los ultimops 20 registros
#print(asistenciaDataFrame.tail(20))

#Obtener resumen estadistico
#print(asistenciaDataFrame.describe())

#cuenta los valores vacíos en cada columna.
#print(asistenciaDataFrame.isnull().sum())

#Selecciona una columna del DataFrame llamada estado,devuelve todos los valores de esa columna
#print(asistenciaDataFrame['estado'])

#Cuenta cuántas veces se repite cada valor distinto en esa columna.
#print(asistenciaDataFrame['estado'].value_counts())

#Cuenta cuántas veces aparece cada estrato en la tabla.
#print(asistenciaDataFrame['estrato'].value_counts())

#.value_counts().head(2) → Muestra los 2 valores más repetidos en la columna.
#.head(2)                 → Muestra las 2 primeras filas reales (sin contar repeticiones).
#print(asistenciaDataFrame['estrato'].value_counts().head(2))

