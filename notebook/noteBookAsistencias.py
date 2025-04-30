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

#Tarea: Filtros o consultas detalladas
#1. Encontrar los estudiantes que si asistieron
#estudiantesQueAsistieron=asistenciaDataFrame.query('estado=="asistio"')
#print(estudiantesQueAsistieron)

#2. Encontrar los estudiantes que faltaron
#estudiantesQueFaltaron=asistenciaDataFrame.query('estado=="inasistencia"')
#print(estudiantesQueFaltaron)
#3. Encntrar los estudiantes que llegaron tarde(justificaron la inaxistencia)

#4. Encontrar los estudiantes de estrato 1
#estudiantesEstratoUno=asistenciaDataFrame.query('estrato==1')
#print(estudiantesEstratoUno)
#5. Encontrar los estudiantes de estratos altos(5 y 6)

#6. Encontrar los estudiantes que llegan en metro
#estudiantesMetro=asistenciaDataFrame.query('medio_transporte=="metro"')
#print(estudiantesMetro)
#7. Encontrar los estudiantes que llegaron en bicicleta
#8. Encontrar todos los estudiantes menos los que llegaron a pie
#estudiantesQueNoCaminan=asistenciaDataFrame.query('medio_transporte!="a pie"')
#print(asistenciaDataFrame["medio_transporte"].unique())
#9. Encontrar todos los registros de asistencia de junio
#10.Encontrar todos los estudiantes que usan transportes ecologicos
#11.Encontrar los estudiantes q usan bus y son de estrato alto 
#12.Encontrar los estudiantes q usan bus y son de estrato bajo
#13.Encontrar estudiantes que caminan para llegar a clases

#Conteo por agrupaciones
#1.Conteo de registros por estado de asistencia
conteo=asistenciaDataFrame.groupby('estado').size()
print(conteo)
#2.Obtener el numero de registros por estrato
#3.Cantidad de estudiantes por medio de transporte
#4.Promedio de estrato por estado de asistencia
#5.Maximo estrato por estado
#6.Minimo estarto por estado
#7.Conteo de asistencias por grupo y estado
