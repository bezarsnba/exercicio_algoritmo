# -*- coding:  LATIN -*-
#Exercicio 7
#Fa�a um algoritmo que calcule a quantidade de litros de combust�vel gasta em
#uma viagem, utilizando um autom�vel que faz 12Km por litro. Para obter o
#c�lculo, o usu�rio deve fornecer o tempo gasto na viagem e a velocidade m�dia
#durante ela. Desta forma, ser� poss�vel obter a dist�ncia percorrida com a
#f�rmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da dist�ncia,
#basta calcular a quantidade de litros de combust�vel utilizada na viagem com a
#f�rmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os
#valores da velocidade m�dia, tempo gasto na viagem, a dist�ncia percorrida e a
#quantidade de litros utilizada na viagem.


TempoGasto = float(raw_input("Digite o tempo gasto"))
VelocidadeMedia = float(raw_input("Digite a velocidade media do automovel"))


#Transformando hora em minutos

Distancia =  TempoGasto * VelocidadeMedia

Litros_usados = Distancia / 12

print "Distancia: {0}km".format(Distancia)
print "Tempo Gasto: {0}".format(TempoGasto)
print "Velocidade Media: {0}km".format(VelocidadeMedia)
print "Litros Utilizado: {0}lt".format(Litros_usados)