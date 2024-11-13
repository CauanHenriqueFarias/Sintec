Lista_de_jogos = {1:{"Nome":"Super Mario", "Valor":35.00},
            2:{"Nome":"Sonic Dash","Valor":20.00},
            3:{"Nome":"GTA San Andreas","Valor":50.00},
            4:{"Nome":"Mega Man V","Valor":15.00}}
print('''
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀▀▄▄▄▄▄░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░
░░░░░█▀▀▀▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐▀▀▀█▄░░░░░░░░▐▌░░░░░░░░░░░░░░
░░░▌█░░░░░░░░█░░░░░░░░░░░░░░░▄█▀░░░░░░█░░░░░░▄▄▄░░░░▐▌░░░░█░░░░░░██▐░░░░░█▀▀█▀▄▄░░
░░░█░░░░░░░░░░▌░░░░░██░░░░░█▀░░░░░░░░░░▌░░░░█░░░░▌░░▐▌░░░░░█░░░░█▀░░█░░░▐░░░░░░░░█
░░░█░░░░░░░░░░▌░░░░░█▌░░░█░░░░░░░░░░░█░█░░░░█░░▄█░░░▐▌░░░░░░▌░░░█▄▄▄██░░█░░░░░░░░░
░░▐▌░░▄▄▄▄▄▄▄█░░░░░██░░░█░░░░░░░░░░░█▄▄█░░░▐█▀▀█░░░░▐▌░░░░░░▌░░▐░░░░░█░░█░░░░░░░░░
░░▐▌░░░░░█░░░░░░░░░█░░░░█▄░░░░░░░░░▌░░░░▌░░░▌░░░▌░░░░█░░░░░█░░░▌░░░░░░█░░█░░░░░░░█
░░█▌░░░░░▐░░░░░░░░▐█░░░░░░▀▀▀▀░░░░█░░░░░░░░░░░░░░░░░░▐██▀▀▀░░░░░░░░░░░░░░░▀▀▄▄▄▀░░
░░█░░░░░░▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐▄░░░░░░▄█░░░░░░▄▄░░░░█▀▀▀▀▀█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▄▄▀▀░░░░░░░░░░█░█░░░░░░▐░█░░░▄█░▐░░░░░█░░░░░█░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░█░░░█░░░░░▐░░▀▄█░░░▐░░░░█░░░░░░█▄░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▐░░░░░███░░░░░▐▌▀▀▀▀█░░░░▐░░░░░░░░░▌░░█░▀▀▀░░░░░▀▄▄░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█▄▄░░░░▀░░░░▐█░░░░░░▌░░░▐░░░░░░░░░▌░░▌░░░░░░░░░░░░▀█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░░░░░░░░░░░░░░░▐░░░░░░░░░█░░░▀█▄▄▄▄░░░░░░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░

1. Ver catalogo de jogos
2. Alterar estoque
3. Vender jogo
4. Sair  
-------------------                      
      ''')
Escolha=int(input("O que voce deseja? " ))
print(20*("-"))


if Escolha == 1:    #Escolha de numero 1 (Mostra a lista de jogos)
  for c,v in Lista_de_jogos.items():
        print(f"{c}: {v["Nome"]} - R${v["Valor"]}")


if Escolha ==2:              #Escolha de numero 2 (Permite modificar o estoque)
    Mudanca=int(input('''
1. Remover um jogo
2. Adicionar um jogo '''))
    

    if Mudanca == 1:           #Permite Remover um jogo
        for c,v in Lista_de_jogos.items():
            print(f"{c}: {v["Nome"]} - R${v["Valor"]}")
        print(20*("-"))
        Item=int(input("Digite o numero de item que deseja remover "))
        Lista_de_jogos.pop(Item)
        for c,v in Lista_de_jogos.items():
            print(f"{c}: {v["Nome"]} - R${v["Valor"]}")

    
    if Mudanca == 2:                      #Permite adicionar um jogo
        Numero=int(input("Em qual numero voce quer adicionar o jogo?"))
        print(20*("-"))
        Lista_de_jogos[Numero]={"Nome":input("Qual o nome do jogo?: "), "Valor":float(input("Qual o valor do jogo?: "))}
        print(20*("-"))
        for c,v in Lista_de_jogos.items():
            print(f"{c}: {v["Nome"]} - R${v["Valor"]}")


if Escolha == 3:      #Escolha de numero 3 (Vende um dos jogos)
    for c,v in Lista_de_jogos.items():
            print(f"{c}: {v["Nome"]} - R${v["Valor"]}")
    print(20*("-"))

    Numero=int(input("Digite o numero do jogo que voce deseja vender "))
    print(f"O jogo {Lista_de_jogos[Numero]["Nome"]} foi vendido por {Lista_de_jogos[Numero]["Valor"]}")
    Lista_de_jogos.pop(Numero)


if Escolha == 4:   #Escolha de numero 4 (Sai do site)
    print("Voce saiu do site.")
