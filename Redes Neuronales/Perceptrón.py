# Perceptrón simple

from sklearn.linear_model import Perceptron # type: ignore

X = [[0,0], [0,1], [1,0], [1,1]]
y = [0,0,0,1]

modelo = Perceptron()pip install scikit-learn tensorflow numpy

modelo.fit(X, y)

print(modelo.predict([[1,1]]))