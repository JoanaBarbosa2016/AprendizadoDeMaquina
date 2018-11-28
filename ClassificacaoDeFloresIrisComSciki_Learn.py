# -*- coding: cp1252 -*-
# Se seu computador n�o tem as bibliotecas, fa�a o download do PIP, que � 
# um gerenciador de pacotes do Python. 

# Importa os conjuntos de dados com problemas de exemplo do Scikit-Learn
from sklearn import datasets

# Importa o classificador SVM
from sklearn import svm

# Carrega os dados do problema Iris
iris = datasets.load_iris()

# Instancia um classificador baseado em SVMs.
classificador = svm.SVC(gamma=0.001, C=100.)

# Treina o classificador com m-1 observa��es e m-1 etiquetas.
classificador.fit(iris.data[:-1], iris.target[:-1])

# Realiza a previs�o da �ltima observa��o (que n�o foi usada 
# durante a fase de treino).
previsao = classificador.predict(iris.data[-1:])

# Valor previsto � igual ao valor da etiqueta para a �ltima observa��o?
# True ou False?
previsao == iris.target[-1:]
