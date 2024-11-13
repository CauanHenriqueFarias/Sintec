 # dicionario= dict (Nome="Tiago", Idade=19, Sexo="Masculino")         #Criacao de dicionarios
# dicionario= {"Nome":"Tiago", "Idade":19, "Sexo":"Masculino"}

# print(dicionario)
# print(dicionario.get("Nome"))
# dicionario["Idade"] = 20     #Atualiza os dados
# print(dicionario["Idade"])   #Printa os dados
# print(dicionario["Sexo"]) 
# print(dicionario.values())
# dicionario.update({"Idade":19})

# del dicionario
# dicionario.pop("Sexo")
# dicionario.popitem()
# dicionario.clear()

# dicionario={"Nome":input("Qual o seu nome?: "), "Idade":int(input("Quantos anos voce tem?: ")), "Sexo":input("Qual o seu sexo?: ")}

# print(dicionario.keys())
# print(dicionario.values())
# print(dicionario.items())

# dicionario = {1:"Bianca", 2:"Jenifer e Lukinhas", 3:"Lee", 4:"Cassio", 5:"Felipe Artilheiro"}

# for i in dicionario:
#     print(f"A chave e: {i} e o seu valore {dicionario[i]}")


# dicionario = {1:{"Nome":"Cauan", "Nota": 100},
#               2:{"Nome":"Vinicius", "Nota":80},
#               3:{"Nome":"Eduardo", "Nota":60}}


# for c,v in dicionario.items():
#     print(f"{c} - {v["Nome"]}")

# while True:
#     escolha = int(input("Qual o numero do aluno(a) que voce quer descobrir a nota?: "))
#     if escolha in dicionario:
#         break
#     print("Aluno(a) nao encontrado tente novamente")

# print(f"A nota do(a) {dicionario[escolha]["Nome"]} e: {dicionario[escolha]["Nota"]}"

Valor=0
Cardapio = {1:{"Nome":"Bolinha de queijo", "Valor":1.50},
            2:{"Nome":"Coxinha de frango","Valor":1.25},
            3:{"Nome":"Risoles de carne","Valor":1.75},
            4:{"Nome":"Pastel de carne","Valor":1.00}}

while True:
    for c,v in Cardapio.items():
        print(f"{c}: {v["Nome"]} - R${v["Valor"]}")
    print(20*"-")

    Pedido= Cardapio[int (input("Qual vai ser o pedido?: "))]["Valor"]
    print(20*"-")

    Quantidade=int(input("Qual vai ser a quantidade?: "))
    print(20*"-")

    Preco = Pedido * Quantidade
    print(f"O valor desse pedido e {Preco}")
    print(20*"-")

    Valor += Preco
    print(f"O valor total ate agora e {Valor}")
    print(20*"-")

    Resposta=input("Deseja Fazer outro pedido?: ").title().strip()
    if Resposta == "Nao":
        break

print(20*"-")
print(f"O total deu {Valor}")








Lista_de_jogos = {1:{"Nome":"Super Mario", "Valor":35.00},
            2:{"Nome":"Sonic Dash","Valor":20.00},
            3:{"Nome":"GTA San Andreas","Valor":50.00},
            4:{"Nome":"Mega Man V","Valor":15.00}}