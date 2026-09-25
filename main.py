def calcular_lucro_mel(peso_bruto, peso_caixa, preco_kg):
    peso_liquido = peso_bruto - peso_caixa
    valor_bruto = peso_liquido * preco_kg
    if peso_liquido > 20:
        desconto = valor_bruto * 0.10
        valor_final = valor_bruto + desconto
    else:
        valor_final = valor_bruto
    return valor_final

peso_b = 25.0
peso_c = 1.5
preco = 40.0
resultado = calcular_lucro_mel(peso_b, peso_c, preco)
print(f"Lucro total: R$ {resultado:.2f}")