# -*- coding: cp1252 -*-
# Se seu computador não tem as bibliotecas, faça o download do PIP, que é 
# um gerenciador de pacotes do Python. 

# Importa os conjuntos de dados com problemas de exemplo do Scikit-Learn
from sklearn import datasets

# Importa o classificador SVM
from sklearn import svm

# Carrega os dados do problema Iris
iris = datasets.load_iris()

# Instancia um classificador baseado em SVMs.
classificador = svm.SVC(gamma=0.001, C=100.)

# Treina o classificador com m-1 observações e m-1 etiquetas.
classificador.fit(iris.data[:-1], iris.target[:-1])

# Realiza a previsão da última observação (que não foi usada 
# durante a fase de treino).
previsao = classificador.predict(iris.data[-1:])

# Valor previsto é igual ao valor da etiqueta para a última observação?
# True ou False?
previsao == iris.target[-1:]
