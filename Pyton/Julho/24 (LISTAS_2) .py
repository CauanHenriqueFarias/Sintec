# n_1 = [2, 4, 6, 8]
# n_2 = int(input("Digite o numero que deseja verificar: "))

# if n_2 in n_1:
#     print("Numero encontrado")
# else:
#     print("Numero nao encontrado")

# numero = [2, 4, 6, 8]
# numero.insert(4, 10)
# numero.append(12)
# print(numero)
# nomes = ["Pedro", "Andre", "Bruna", "Sara"]
# print(nomes)
# print(sorted(nomes))
# print(sorted(nomes, reverse = True))

# nomes = []
# idades = []
# n1= input("Digite um nome: ")
# n2= input("Digite um nome: ")
# n3= input("Digite um nome: ")
# n4= input("Digite um nome: ")
# n5= input("Digite um nome: ")

# nomes = [n1, n2, n3, n4, n5]
# nomes = sorted(nomes)
# print(nomes)

# i1 = int(input("Digite a idade"))
# i2 = int(input("Digite a idade"))
# i3 = int(input("Digite a idade"))
# i4 = int(input("Digite a idade"))
# i5 = int(input("Digite a idade"))

# idade = [i1, i2, i3, i4, i5]
# idade = sorted(idade, reverse=True)
# print(idades)

# nomes = []
# for i in range (5):
#     nomes.append (input("Digite um nome: ").title().strip())

# idade= []
# for i in range(5):
#     idade.append (input("Digite uma idade: ").strip())

# print (sorted(nomes))
# print (sorted(idade, reverse = True))

# animais = ["Cachorro", "Gato", "Passaro", "Pato", "Tigre", "Tatu"]

# animais.remove("Gato") #Deleta o que voce escolhe por "nome"
# print(animais)

# animais.pop() #Deleta a ultima palavra
# print(animais)

# animais.pop(1) #Deleta o que voce escolhe por "indice"
# print(animais)

# del animais[0] #Deleta o que voce escolhe por "indice"
# print(animais)

# animais.clear() #Deleta dentro da lista

# del animais #Deleta a lista inteira
# print(animais)

cores = ["Azul", "Verde", "Amarelo", "Roxo"]
# print(cores)

# cores.remove("Verde")
# cores.remove("Roxo")
# print(cores)

# cores.append("Verde")
# cores.insert(0,"Rosa")
# print(cores)

# cores.clear()
# print(cores)

i= 0
while i<len(cores):
    print(cores[i])
    i+=1
print(20*"-")

[print(cores[elemento]) for elemento in range(len(cores))]
print(20*"-")
[print(i) for i in cores]

for j in range(3):
    for i in range(len(cores)):
        print(cores[i])
    print(20*"-")