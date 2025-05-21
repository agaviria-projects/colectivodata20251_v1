import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Grafica de barras
colores=["#33f800","#00da71","#00b799","#2f4858","#0092a0"]

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

plt.figure(figsize=(8,5))
sns.countplot(x='estado',data=dataFrameAsistencia,palette=colores)
plt.title("Cantidad de registros por estado")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()


#Grafica de Torta
conteoTransporte=dataFrameAsistencia['medio_transporte'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    conteoTransporte,
    labels=conteoTransporte.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("Blues")
)
plt.title("Distribucion por medio de transporte")
plt.tight_layout()
plt.show()

#Barras Agrupadas
plt.figure(figsize=(10,6))
conteoEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)
conteoEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,6),
    color=colores
)
plt.title("Registros por estado y medio de transporte")
plt.xlabel=("Estados de asistencias")
plt.ylabel=("Medio de transporte")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#Grafico de Linea
promedioTransporte=dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean().sort_values()
plt.figure(figsize=(10,5))
plt.plot(promedioTransporte.index,promedioTransporte.values,marker='o',linestyle='-',color="#33f800")
plt.title("Promedio de estrato por medio de transporte")
plt.xlabel("Medio de transporte")
plt.ylabel("Estrato promedio")
plt.grid(True)
plt.tight_layout()
plt.show()