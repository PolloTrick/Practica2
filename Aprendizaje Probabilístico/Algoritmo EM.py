# EM usando Gaussian Mixture

from sklearn.mixture import GaussianMixture # type: ignore
import numpy as np # type: ignore

X = np.array([[1], [2], [3], [10], [11], [12]])

modelo = GaussianMixture(n_components=2)

modelo.fit(X)

print("Clusters:", modelo.predict(X))