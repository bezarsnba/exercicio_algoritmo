# -*- coding:  LATIN -*-
#Fa�a um algoritmo que leia quatro n�meros e apresente os resultados de adi��o
#e multiplica��o dos valores entre si, baseando-se na utiliza��o da propriedade
#distributiva, ou seja, se forem lidas as vari�veis A, B, C e D, devem ser somadas
#e multiplicadas A com B, A com C e A com D; B com C, B com D e por �ltimo C
#com D.


A = raw_input("Digite um numero para A")
B = raw_input("Digite um numero para B")
C = raw_input("Digite um numero para C")
D = raw_input("Digite um numero para D")

Escolha = input('Escolha uma letra para utilizar')


if Escolha == A:
    print A
#        A x B and A + B
#        A x C and A + C
#        A x D And A + D

elif Escolha == B:
    print B
#        B x C and B + C
#        B x D and B + D

elif Escolha == C:
    print C
#        C x D and C + D
else:
    try:
       print "Escolha"
    except NameError:
       print "Nao encontrado"
