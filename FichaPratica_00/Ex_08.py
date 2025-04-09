#Pedir ao user a duração da música em min e seg

minfaixa1 = int(input("Digite os minutos: "))
segfaixa1 = int (input("Digite os segundos: "))

minfaixa2 = int(input("Digite os minutos: "))
segfaixa2 = int (input("Digite os segundos: "))

minfaixa3 = int(input("Digite os minutos: "))
segfaixa3 = int (input("Digite os segundos: "))

minfaixa4 = int(input("Digite os minutos: "))
segfaixa4 = int (input("Digite os segundos: "))

minfaixa5 = int(input("Digite os minutos: "))
segfaixa5 = int (input("Digite os segundos: "))


totSeg = 0

#Somar os segundos e minutos
somaSeg = (segfaixa1 +  segfaixa2 + segfaixa3 + segfaixa4 + segfaixa5)
somaMin = (minfaixa1 + minfaixa2 + minfaixa3 + minfaixa4 + minfaixa5) 

#Converter a duração para segundos
totSeg += (somaMin * 60) + somaSeg

#Calcular segundos, minutos, e horas
horas= totSeg // 3600
minutos= (totSeg%3600)//60
segundos= totSeg%60

#Apresentar o resultado
print(F"Tempo total: ")
