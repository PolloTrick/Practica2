# Redes de Decisión

def calcular_valor_esperado(prob_exito, ganancia, perdida):
    return (prob_exito * ganancia) + ((1 - prob_exito) * perdida)

print("=== REDES DE DECISIÓN ===")

# Opción 1
valor_a = calcular_valor_esperado(0.7, 1000, -500)

# Opción 2
valor_b = calcular_valor_esperado(0.5, 1500, -200)

print(f"Valor esperado Opción A: {valor_a}")
print(f"Valor esperado Opción B: {valor_b}")

if valor_a > valor_b:
    print("La mejor decisión es: Opción A")
else:
    print("La mejor decisión es: Opción B")