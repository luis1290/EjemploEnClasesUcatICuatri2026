import pandas as pd # importar a biblioteca pandas para manipulação de dados
import numpy as np # importar a biblioteca numpy para operaciones  numéricas
import matplotlib.pyplot as plt # importar a biblioteca matplotlib para visualização de dados
from sklearn.model_selection import train_test_split # importar a función  train_test_split para dividir os dados em conjuntos de treinamento e teste
from sklearn.tree import DecisionTreeClassifier # importar a classe DecisionTreeClassifier para crear um modelo de árvore de decisión 
from sklearn.metrics import accuracy_score # importar a función accuracy_score para avaliar a precisión de modelo
from sklearn.cluster import KMeans # importar a classe KMeans para realizar clustering para agrupación de dados

#cargar el dataset
data = pd.read_csv('datos_estudiantes.csv') # cargar o dataset a partir de um arquivo CSV

#Explorar los datos
print(data.info()) # mostrar información sobre o dataset
print(data.describe()) # mostrar estadísticas descriptivas do dataset

# visualización de datos
plt.scatter(data['horas_estudio'], data['nota_final']) # crea un gráfico de dispersión entre horas de estudio y nota final
plt.xlabel('Horas de Estudio') # etiqueta para el eje x
plt.ylabel('Nota Final') # etiqueta para el eje y
plt.show() # mostrar el gráfico

#preparación de datos para el modelo de clasificación
data['aprobado'] = data['nota_final'].apply(lambda x: 1 if x >= 60 else 0) # crear una nueva columna 'aprobado' que indica si el estudiante aprobó o no
x = data[['horas_estudio','asistencia']] # seleccionar las características para el modelo
y = data['aprobado'] # seleccionar la variable objetivo para el modelo

#dividir los datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) # dividir los datos en conjuntos de entrenamiento y prueba

#entrenar el modelo de árbol de decisión
model = DecisionTreeClassifier() # crear una instancia del modelo de árbol de decisión
model.fit(x_train, y_train) # entrenar el modelo con los datos de entrenamiento

#predecir con el modelo
y_pred = model.predict(x_test) # hacer predicciones con el modelo utilizando los datos de prueba
accuracy = accuracy_score(y_test, y_pred) # calcular la precisión del modelo
print(f'Precisión del modelo: {accuracy}') # mostrar la precisión del modelo

#prueba maunal del modelo
nuevo_estudiante = [[5, 80],[5, 70], [5, 90]] # crear un nuevo estudiante con horas de estudio y asistencia
predicciones = model.predict(nuevo_estudiante) # hacer predicciones para el nuevo estudiante
print(f'Predicciones para el nuevo estudiante: {predicciones}') # mostrar las predicciones para el nuevo estudiante




#clustering con KMeans
kmeans = KMeans(n_clusters=30) # crear una instancia del modelo KMeans con 3 clusters
kmeans.fit(x)
data['cluster'] = kmeans.labels_ # asignar las etiquetas de cluster a los datos
print(data.head()) # mostrar las primeras filas del dataset con las etiquetas de cluster
print(data['cluster'].value_counts()) # mostrar la cantidad de estudiantes en cada cluster
print(kmeans.cluster_centers_) # mostrar los centros de los clusters



centro = kmeans.cluster_centers_ # obtener los centros de los clusters
plt.scatter(centro[:, 0], centro[:, 1], marker='X', s=200) # graficar los centros de los clusters

#etiquetas
plt.xlabel('Horas de Estudio') # etiqueta para el eje x
plt.ylabel('Nota Final') # etiqueta para el eje y
plt.title('Clustering de Estudiantes') # título del gráfico
plt.show() # mostrar el gráfico de clustering

