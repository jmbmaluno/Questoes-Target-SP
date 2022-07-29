#Gerando variáveis
f1 = 0
f2 = 1
aux = f1

#Recebendo o valor
numero = int(input("Dê o valor que você deseja consultar: "))

#Calculando a sequência até que f1 ser igual ou maior que o numero
while f1 < numero:
	aux = f2
	f2 = f1+f2
	f1 = aux

#Como o while acabou então ou f1 é igual ao número ou ele é maior que o número e o número não está na sequência
if f1 == numero:
	print("Esse número faz parte da sequência de Fibonacci")
	
else:
	print("Esse número NÂO faz parte da sequência de Fibonacci")
