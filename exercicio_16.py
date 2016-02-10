#/usr/bin/python2.7
# -*- coding:  LATIN -*-
#Faça um algoritmo que leia dois numeros inteiros A e B, atribui a uma variavel
#chamada MAIOR ou maior entre os dois numeros lidos e em MENOR o menor deles,
# e imprima os valores lidos contendo o MAIOR e MENOR

numReceb = raw_input("Digite 2 numeros: ")

inputList = numReceb.split()
inputList= [int(I) for I in inputList] 

A=inputList[0]
B=inputList[1]

if A > B:
    maior = A
    menor = B

else:
    maior = B
    menor = A

print "Numeros Lidos {} {}" .format(A, B)
print "Maior {0}".format(maior)
print "Menor {0}".format(menor)

