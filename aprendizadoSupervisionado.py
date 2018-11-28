# -*- coding: cp1252 -*-
"importe o m�dulo tree do Sklearn"
from sklearn import tree
"atributos que voc� deseja usar para classificar os animais"
features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]]
"Defina a sa�da que cada classificador ter�. Uma galinha ser� ouum cavalo"
labels = ["chicken", "chicken", "horse", "horse"]
"classificador, que ser� baseado em uma �rvore de decis�o."
classif = tree.DecisionTreeClassifier()
"Alimente ou ajuste seus dados para o classificador."
classif.fit(features, labels)
"""Podemos agora prever resultados a partir de um determinado conjunto de
dados. A seguir � mostrado como prever qual animal
tem uma altura de 7 polegadas, 0,6 kg de peso e uma temperatura de 41 �C:"""
print classif.predict([[7, 0.6, 41]])
"""Agora, � mostrado como prever qual animal tem uma altura de 38 polegadas,
600 kg de peso e uma temperatura de 37.5 �C:"""
print classif.predict([[38, 600, 37.5]])
"""Como voc� pode ver acima, voc� treinou o algoritmo para aprender todos os
atributos e os nomes dos animais,e o conhecimento obtido com esses dados �
usado para testar novos animais."""
