# SVM

from sklearn import svm # type: ignore

X = [[0,0], [1,1]]
y = [0,1]

modelo = svm.SVC(kernel='linear')

modelo.fit(X, y)

print(modelo.predict([[0.8,0.8]]))