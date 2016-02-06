# -*- coding:  LATIN -*-
#Exercicio 7
#Faça um algoritmo que calcule a quantidade de litros de combustível gasta em
#uma viagem, utilizando um automóvel que faz 12Km por litro. Para obter o
#cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média
#durante ela. Desta forma, será possível obter a distância percorrida com a
#fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância,
#basta calcular a quantidade de litros de combustível utilizada na viagem com a
#fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os
#valores da velocidade média, tempo gasto na viagem, a distância percorrida e a
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