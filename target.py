-Questao 1:
Valor final de SOMA: 91

-Questao 2:

def fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return f"{num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{num} não pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
print(fibonacci(numero))

-Questao 3:

import json


faturamento_diario = {
    "dias": [
        {"dia": 1, "valor": 22174.1664},
        {"dia": 2, "valor": 24537.6698},
        {"dia": 3, "valor": 26139.6134},
        {"dia": 4, "valor": 0.0},
        {"dia": 5, "valor": 0.0},  
        {"dia": 6, "valor": 26742.6612},
      
    ]
}


valores = [dia['valor'] for dia in faturamento_diario['dias'] if dia['valor'] > 0]
menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)
dias_acima_media = sum(1 for v in valores if v > media)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

-Questao 4:


faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}% do total")


-Questao 5:

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida


string = input("Informe uma string: ")
print("String invertida:", inverter_string(string))

