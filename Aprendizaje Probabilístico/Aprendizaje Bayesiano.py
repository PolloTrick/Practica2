# Aprendizaje Bayesiano simple

# Probabilidades iniciales
P_H = 0.6
P_E_dado_H = 0.7
P_E = 0.5

# Bayes
P_H_dado_E = (P_E_dado_H * P_H) / P_E

print("Probabilidad posterior:", P_H_dado_E)