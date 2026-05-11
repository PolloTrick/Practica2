# Clustering jerárquico

from sklearn.cluster import AgglomerativeClustering # type: ignore
import numpy as np # type: ignore

X = np.array([
    [1,2], [2,2], [8,8], [9,9]
])

modelo = AgglomerativeClustering(n_clusters=2)

etiquetas = modelo.fit_predict(X)

print(etiquetas)