# Clustering no supervisado

from sklearn.cluster import KMeans # type: ignore
import numpy as np # type: ignore

X = np.array([
    [1,2], [1,1], [2,1],
    [10,10], [10,11], [11,10]
])

modelo = KMeans(n_clusters=2, random_state=0)

modelo.fit(X)

print("Etiquetas:", modelo.labels_)