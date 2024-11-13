import random

print("SEJA BEM VINDO AO JOGO DE PAR OU IMPAR!!!")
vitorias=int(input("Quantas vitorias ate ganhar?: "))
vitorias_usuario = 0
vitorias_computador = 0

while vitorias_usuario <vitorias and vitorias_computador <vitorias:
    while True:
        print("----------")
        tipo=int(input(f"Par ou Impar? (Digite 1 ou 2 para sua resposta) \n[1]. Par: \n[2]. Impar:\n"))
        if tipo != 1 and tipo !=2:
            print("Resposta invalida tente novamente")
        else:
            break
    
    n_1=int(input(f"---------- \nDigite um numero: "))
    n_2=(random.randint(1,2))
    print(f"---------- \nO computador escolheu {n_2}")
    resultado=n_1+n_2
    
    if tipo == 1 and (resultado)%2==0:
        print(f"---------- \n{resultado} e par, voce ganhou")
        vitorias_usuario += 1
    if tipo == 1 and (resultado)%2==1:
        print(f"---------- \n{resultado} e impar, voce perdeu")
        vitorias_computador += 1
    if tipo == 2 and (resultado)%2==1:
        print(f"---------- \n{resultado} e impar, voce ganhou")
        vitorias_usuario += 1
    if tipo == 2 and (resultado)%2==0:
        print(f"---------- \n{resultado} e par voce perdeu")
        vitorias_computador += 1

    print(f"---------- \nPlacar: Você {vitorias_usuario} x {vitorias_computador} Computador")
    if vitorias_usuario == vitorias:
        print(f"---------- \nVocê venceu! Parabéns!")
    if vitorias_computador == vitorias:
        print(f"---------- \nO computador venceu. Melhor sorte na próxima vez!")


# import random
# cont_jogador= 0
# cont_computador= 0

# while True:
#     escolha= input("Par ou impar?: ").lower().strip()
#     numero= int(input("Digite um numero?: "))
#     computador=random.randint(0,10)
#     print(f"Computador escolheu{computador}")
#     resultado= numero+computador

#     if ((resultado%2==0) and (escolha=="par")) or ((resultado%2==1) and (escolha=="impar")):
#         cont_jogador=cont_jogador+1
#         print("Voce venceu")
#     if ((resultado%2==1) and (escolha=="par")) or ((resultado%2==0) and (escolha =="par")):
#         cont_computador=cont_computador+1
#         print("O computador venceu")
#     if cont_jogador==2:
#         print("Voce venceu a melhor de 3")
#         break
#     if cont_computador==2:
#         print("O computador venceu a melhor de 3")
#         break







