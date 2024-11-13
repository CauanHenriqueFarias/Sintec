# nome1 = "Lucas"
# nome2 = "Joao"
# nome3 = "Ana"
# idade1 = 13
# idade2 = 16
# idade3 = 23
# altura1 = 1.58
# altura2 = 1.75
# altura3 = 1.63
# print(f"{nome1} tem {idade1} anos de idade, e {altura1} metros de altura")
# print(f"{nome1} tem {idade2} anos de idade, e {altura2} metros de altura")
# print(f"{nome1} tem {idade3} anos de idade, e {altura3} metros de altura")


nome = ["Lucas", "Joao", "Ana", "Zuleika", "Cauan"]
idade = [13, 16, 23, 92, 17]
altura = [1.58, 1.75, 1.63, 1.90, 1.80]
maioridade = [False, False, True, True, False]
lista_das_listas = [nome, idade, altura, maioridade]

for i in range(len(nome)):
    print(f"{nome[i]} tem {idade[i]} anos de idade e {altura[i]} metros de altura")

lista_1 = ["Lucas," , 13 , 1.58, False]
lista_2 = ["Joao" , 16 , 1.75 , False]
lista_3 = ["Ana" , 23 , 1.63 , True]
lista_4 = ["Zuleika" , 92 , 1.90 , True]
lista_5 = ["Cauan" , 17 , 1.80 , False]

print(lista_das_listas[2][2])
if "Lucas" in nome:
    print("Nome encontrado")
else:
    print("Nome nao encontrado")