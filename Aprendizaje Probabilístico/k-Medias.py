# k-Means

from sklearn.cluster import KMeans # type: ignore
import numpy as np # type: ignore

X = np.array([
    [1,2], [1,1], [2,2],
    [8,8], [9,8], [8,9]
])

modelo = KMeans(n_clusters=2)

modelo.fit(X)

print(modelo.cluster_centers_)