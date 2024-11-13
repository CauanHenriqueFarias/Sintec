import random

lista = ["Felipe", "Bianca", "Julia"]
# cont = 0

print(f" {20*"-"}LISTA DE PARTICIPANTES {20*"-"}")

for i in lista:
    print(f".{i}")
print(f"{20*"-"}ORDEM DAS APRESENTACOES {20*"-"}")

# while True:

#     cont+=1
#     nome=lista[random.randint(0,len(lista)-1)]
#     print (f"{cont}-{nome}")
#     lista.remove(nome)

#     if lista == []:
#         break
#     if int(input("Para continuar digite 1: ")) != 1:
#         break

for i in range(len(lista)):
    nome=lista[random.randint(0,len(lista)-1)]
    print (f"{i+1}-{nome}")
    lista.remove(nome)

    input("Aperte ENTER para sortear outra pessoa")