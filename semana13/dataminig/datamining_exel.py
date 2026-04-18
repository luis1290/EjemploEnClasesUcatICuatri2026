import pandas as pd # importar a biblioteca pandas para manipulação de dados
import numpy as np # importar a biblioteca numpy para operaciones  numéricas
import matplotlib.pyplot as plt # importar a biblioteca matplotlib para visualização de dados
from sklearn.model_selection import train_test_split # importar a función  train_test_split para dividir os dados em conjuntos de treinamento e teste
from sklearn.tree import DecisionTreeClassifier # importar a classe DecisionTreeClassifier para crear um modelo de árvore de decisión 
from sklearn.metrics import accuracy_score # importar a función accuracy_score para avaliar a precisión de modelo
from sklearn.cluster import KMeans # importar a classe KMeans para realizar clustering para agrupación de dados

#cargar el dataset
data = pd.ExcelFile('datos_estudiantes.xlsx') # cargar o dataset a partir de um arquivo Excel

#Explorar los datos
print(data.info()) # mostrar información sobre o dataset
print(data.describe()) # mostrar estadísticas descriptivas do dataset

# visualización de datos
plt.scatter(data['horas_estudio'], data['nota_final']) # crea un gráfico de dispersión entre horas de estudio y nota final
plt.xlabel('Horas de Estudio') # etiqueta para el eje x
plt.ylabel('Nota Final') # etiqueta para el eje y
plt.show() # mostrar el gráfico