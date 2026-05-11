# Independencia condicional

# Si A y B son independientes dado C:
# P(A y B | C) = P(A | C) * P(B | C)

P_A_dado_C = 0.6
P_B_dado_C = 0.5

resultado = P_A_dado_C * P_B_dado_C

print("P(A y B | C):", resultado)