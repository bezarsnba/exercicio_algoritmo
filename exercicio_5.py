# -*- coding:  LATIN -*-
#Exercicio 5
#Faça um algoritmo que leia uma temperatura em graus Celsius e apresente-a
#convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5,
#na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius.


GrausCelsios=int(raw_input("Digite a Temperatura em C"))
GraulsFahrenheit=int(raw_input("Digite a Temperatura em F"))


F = ( 9 * GrausCelsios + 160 ) /5

C= ( GraulsFahrenheit - 32  ) * ( 5.0 / 9.0 )


print "Temperatura em {0}°F e {1}°C ".format(F, GrausCelsios)
print "Temperatura em %.1i°C e %d°F" % (C , GraulsFahrenheit )
