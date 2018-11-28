# -*- coding: cp1252 -*-
"importe o módulo tree do Sklearn"
from sklearn import tree
"atributos que você deseja usar para classificar os animais"
features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]]
"Defina a saída que cada classificador terá. Uma galinha será ouum cavalo"
labels = ["chicken", "chicken", "horse", "horse"]
"classificador, que será baseado em uma árvore de decisão."
classif = tree.DecisionTreeClassifier()
"Alimente ou ajuste seus dados para o classificador."
classif.fit(features, labels)
"""Podemos agora prever resultados a partir de um determinado conjunto de
dados. A seguir é mostrado como prever qual animal
tem uma altura de 7 polegadas, 0,6 kg de peso e uma temperatura de 41 ºC:"""
print classif.predict([[7, 0.6, 41]])
"""Agora, é mostrado como prever qual animal tem uma altura de 38 polegadas,
600 kg de peso e uma temperatura de 37.5 ºC:"""
print classif.predict([[38, 600, 37.5]])
"""Como você pode ver acima, você treinou o algoritmo para aprender todos os
atributos e os nomes dos animais,e o conhecimento obtido com esses dados é
usado para testar novos animais."""
