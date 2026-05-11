# k-NN

from sklearn.neighbors import KNeighborsClassifier # type: ignore

X = [[1], [2], [3], [6], [7], [8]]
y = [0,0,0,1,1,1]

modelo = KNeighborsClassifier(n_neighbors=3)

modelo.fit(X, y)

print(modelo.predict([[5]]))