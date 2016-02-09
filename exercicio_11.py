#/usr/bin/python2.7
# -*- coding:  LATIN -*-
#Faça um algoritmo que leia um valor inteiro e apresente os resultados do
#quadrado e do cubo do valor lido. 
import math

valorInt=input("Digite um numero: ")

valorQuadr = math.sqrt(valorInt)
valorCubo = math.pow(valorInt, 3)

print valorQuadr
print valorCubo
