#/usr/bin/python2.7
# -*- coding:  LATIN -*-
#Faça um algoritmo que leia dois valores inteiros (A e B) e apresente o resultado
#do quadrado da soma dos valores lidos.
import math

valorA=input("Digite um Valor para a Variavel A ")
valorB=input("Digite um Valor para a Variavel B ")

somaValorAB= valorA + valorB

valorQuadr = math.sqrt(somaValorAB)

print "Valor ao quadrado da soma: %.2f " % valorQuadr



