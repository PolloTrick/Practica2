# Inferencia por enumeración

def inferencia(prob_a, prob_b_dado_a):
    return prob_a * prob_b_dado_a

P_A = 0.4
P_B_dado_A = 0.7

resultado = inferencia(P_A, P_B_dado_A)

print("Resultado de inferencia:", resultado)