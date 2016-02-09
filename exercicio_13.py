#/usr/bin/python2.7
# -*- coding:  LATIN -*-
#Faça um algoritmo que leia dois valores inteiros (A e B) e apresente o resultado
#da soma do quadrado de cada valor lido. 
import math
valorA=input("Digite um Valor para a Variavel A ")
valorB=input("Digite um Valor para a Variavel B ")

somaValorAB= valorA + valorB

valorQuadr = math.sqrt(somaValorAB)* somaValorAB

print "Valor soma do quadrado: %.2f " % valorQuadr
