# Atividade 2 - 
## 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_m2 = float(input(" Digite a medida da sua área em m2: "))
print(area_m2)

import math

litro_m2 =  3 
lata_18litros_m2 = 54
valor_lata_reais = 80
txt_valor = " Valor total a pagar: R$"


calc_qnt_lata = area_m2 / lata_18litros_m2
arredond = math.ceil(calc_qnt_lata)
print(" Total de latas necessárias:", arredond )

valor_total_qnt_latas = valor_lata_reais * arredond
print(txt_valor, "{:.2f}".format(valor_total_qnt_latas))
