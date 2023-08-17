# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;

import math

lata = 18
galao = 3.6
lata_valor = 80
galao_valor = 25

area = float(input("Digite a medida da sua area em m2: "))
litros_cliente_com_sobra = (area / 6) * 1.1
qnt_latas_cliente = math.ceil(litros_cliente_com_sobra / lata)
qnt_galao_cliente = math.ceil(litros_cliente_com_sobra / galao)
vlr_lt = qnt_latas_cliente * lata_valor
vlr_gl = qnt_galao_cliente * galao_valor

print(f"Você precisa de {qnt_latas_cliente} latas de tinta. ")
print(f"O preço total das latas será de R$ {vlr_lt:.2f}")
print(f"Você precisa de {qnt_galao_cliente} galões de tinta. ")
print(f"O preço total dos galões será de R$ {vlr_gl:.2f}")


# area = float(input("Digite a medida da sua area em m2: "))
# litros = area/6
# litros_com_folga = litros * 1.1
# lata = int(litros_com_folga/18)
# resto = litros_com_folga % 18
# galoes = math.ceil(resto/3.6)
# preco_lata = lata * 80
# preco_galao = galoes * 25

