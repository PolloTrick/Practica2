# Red Bayesiana simple

prob_enfermedad = 0.01
prob_sintoma_dado_enfermedad = 0.9
prob_sintoma_dado_no_enfermedad = 0.2

# Teorema de Bayes
prob_sintoma = (
    prob_sintoma_dado_enfermedad * prob_enfermedad +
    prob_sintoma_dado_no_enfermedad * (1 - prob_enfermedad)
)

prob_enfermedad_dado_sintoma = (
    prob_sintoma_dado_enfermedad * prob_enfermedad
) / prob_sintoma

print("Probabilidad de enfermedad dado síntoma:",
      prob_enfermedad_dado_sintoma)