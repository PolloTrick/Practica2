# Valor de la Información

print("=== VALOR DE LA INFORMACIÓN ===")

# Sin información
valor_sin_info = 500

# Con información perfecta
valor_con_info = 800

valor_info = valor_con_info - valor_sin_info

print(f"Valor sin información: {valor_sin_info}")
print(f"Valor con información: {valor_con_info}")
print(f"Valor de la información: {valor_info}")

if valor_info > 0:
    print("Sí vale la pena obtener información.")
else:
    print("No vale la pena obtener información.")