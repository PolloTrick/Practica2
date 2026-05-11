# Naive Bayes con sklearn

from sklearn.naive_bayes import GaussianNB # type: ignore

X = [[1,2], [2,3], [3,4], [4,5]]
y = [0, 0, 1, 1]

modelo = GaussianNB()

modelo.fit(X, y)

prediccion = modelo.predict([[2,2]])

print("Predicción:", prediccion)