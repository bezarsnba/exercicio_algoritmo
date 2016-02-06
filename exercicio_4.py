# -*- coding:  UTF-8 -*-
#Exercio 4 :Faça um algoritmo que:
#a) Obtenha o valor para a variável HT (horas trabalhadas no mês);
#b) Obtenha o valor para a variável VH (valor hora trabalhada):
#c) Obtenha o valor para a variável PD (percentual de desconto);
#d) Calcule o salário bruto => SB = HT * VH;
#e) Calcule o total de desconto => TD = (PD/100)*SB;
#f) Calcule o salário líquido => SL = SB – TD;
#g) Apresente os valores de: Horas trabalhadas, Salário Bruto, Desconto, Salário Liquido.

import math
HT=input("Horas Trabalhada")
VH=input("Valor hora Trabalhada")
PD=float(raw_input("Percentual de desconto"))

#Salario bruto
SB =  float(HT * VH)

#Total de desconto
TD = (PD/ 100)*SB

#Salario Liquido
SL = (SB - TD)

print "Horas Trabalhada {0}".format(HT)
print "Salario Bruto R$ %.2f"  % SB
print "Desconto R$ %.2f"  % TD
print "Salario Liquido R$ %.2f"  % SL



