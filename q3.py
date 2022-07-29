#declaração de variaveis
fatura= [31490.7866, 37277.9400, 37708.4303, 0.0000, 0.0000, 17934.2269, 0.0000, 6965.1262, 24390.9374, 14279.6481, 0.0000, 0.0000, 39807.6622, 27261.6304, 39775.6434, 29797.6232, 17216.5017, 0.0000, 0.0000, 12974.2000, 28490.9861, 8748.0937, 8889.0023, 17767.5583, 0.0000, 0.0000, 3071.3283, 48275.2994, 10299.6761, 39874.1073]

maior = fatura[0]
menor = fatura[0]
cont =0

#calculo de media
media = 0
invalido =0
for i in range (30):
	media = media + fatura[i]
	if fatura[i] == 0:
		invalido = invalido+1

#Retirando do calculo da média o dias que são inválidos
media= media/(len(fatura)-invalido)

#Procurando o maior e menor valor. Contando quantos valores estão acima da média
for i in range (30):
	if fatura[i] > maior:
		maior= fatura[i]
		
	if fatura[i] > 0 and fatura[i]<menor:
		menor=fatura[i]
		
	if fatura[i] > media:
		cont=cont+1
		
print("O maior valor de faturamento ocorrido em um dia do mês: " + str(maior))
print("O menor valor de faturamento ocorrido em um dia do mês: " + str(menor))
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: " + str(cont))
