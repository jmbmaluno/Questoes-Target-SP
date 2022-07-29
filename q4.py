#Faturamento na seguinte ordem SP, RJ, MG, ES, OUTROS
faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
ordem = ["SP", "RJ", "MG", "ES", "OUTROS"]
total = 0

#calculando o valor total
for i in range (len(faturamento)):
	total = total + faturamento[i]

print("--Faturamento--")

#Formatando a saída para ser no módelo:
#XX: YY.YY%
#Onde XX é local e YY.YY o faturamento em porcentagem
for i in range(len(faturamento)):
	print("%s: %.2f" %(ordem[i], (faturamento[i]*100/total)) + "%")
