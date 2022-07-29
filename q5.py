#Recebendo a String
palavra = input("Entre a String que será invertida: ")

#Criando um vetor do tamanho da String
invertida = [""] * len(palavra)

resposta = ""

#O laço percorrerá o String recebida da primeira posiçao até a ultima
#e percorrerá o vetor 'invertida' da ultima posição até a primeira
#Dessa forma, será atríbuida o valor da primeira posição da String recebida na ultima posição de "invertida" e o loop continuará até que a primeira posição de "invertida" seja a ultima posição da String recebida
for i in range (len(palavra)):
	invertida[len(palavra) - i - 1] = palavra[i]


for i in range(len(palavra)):
	resposta = resposta + invertida[i]

print("A String %s invertida é %s" %(palavra,resposta))
