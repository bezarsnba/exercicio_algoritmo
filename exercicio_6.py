# -*- coding:  LATIN -*-
#Exercicio 6
# Faça um algoritmo que calcule e apresente o valor do volume de uma lata de
# óleo, utilizando a fórmula VOLUME = 3.14159 * RAIO² * ALTURA.

Raio=float(raw_input("Digite o Raio:"))
Altura=float(raw_input("Digite a Altura"))

VOLUME = ( 3.14159 * (Raio * 2)  * Altura )


print "VOLUME:  %.2f" % VOLUME


