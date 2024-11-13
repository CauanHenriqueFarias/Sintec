aliados = ["Mago", "Rei", "Curandeiro"] #Personagens aliados  lista
Mago=8   #Vida dos aliados
Rei=20
Curandeiro=14
inimigos = ["Feiticeiro", "Imperadador", "Bruxo"] #Personagens inimigos lista
Feiticeiro=8  #Vida dos inimigos
Imperador=20
Bruxo=14
vida_aliados = [Mago, Rei, Curandeiro,]   #Lista com a variavel  da vida dos personagens aliados
vida_inimigos = [Feiticeiro, Imperador, Bruxo,] #Lista com a variavel  da vida dos personagens inimigos
round= 0    #Variavel contadora dos rounds

while True:
    round+=1
    print(20*"-")
    print (f"COMECA O ROUND {round}")      #Comeco de todo round/ escolha de quem ataca
    print(20*"-")
    escolha=int(input(f"Escolha o numero de quem ira atacar: \n[1].Mago\n[2].Rei\n[3].Curandeiro\n"))
    print(20*"-")


    if escolha == 1:#Mago Bate
        
        escolha_alvo=int(input(f"Escolha o numero de quem voce quer atacar \n[1]. Feiticeiro \n[2]. Imperador \n[3]. Bruxo \n "))
        print(20*"-")     #Escolha de alvos

        if escolha_alvo == 1:
            vida_inimigos[0] -= 5
            for i in range(len(vida_inimigos)):
                print(f"{inimigos[i]} tem {vida_inimigos[i]} de vida")
            
        if escolha_alvo == 2:
                vida_inimigos[1] -=5
                for i in range(len(inimigos)):
                    print(f"{inimigos[i]} tem {vida_inimigos[i]} de vida")
            
        if escolha_alvo == 3:
            vida_inimigos[2] -= 5
            for i in range(len(inimigos)):
                print(f"{inimigos[i]} tem {vida_inimigos[i]} de vida")
       

    if escolha == 2: #Rei Bate
        
        escolha_alvo=int(input(f"Escolha o numero de quem voce quer atacar \n[1]. Feiticeiro \n[2]. Imperador \n[3]. Bruxo \n "))
        print(20*"-")
        
        if escolha_alvo == 1:
            vida_inimigos[0] -= 3
            for i in range(len(inimigos)):
                print(f"{inimigos[i]} tem {vida_inimigos[i]} de vida")
        
        if escolha_alvo == 2:
            vida_inimigos[1] -= 3
            for i in range(len(inimigos)):
                print(f"{inimigos[i]} tem {vida_inimigos[i]} de vida")
        
        if escolha_alvo == 3:
            vida_inimigos[2]-= 3
            for i in range(len(inimigos)):
                print(f"{inimigos[i]} tem {vida_inimigos[i]} de vida")
    

    if escolha == 3: #Curandeiro Cura

        escolha_alvo=int(input(f"Escolha o numero de quem voce que r atacar \n[1]. Mago \n[2]. Rei\n "))
        print(20*"-")
        
        if escolha_alvo == 1:
            vida_aliados[0] += 5
            for i in range(len(aliados)):
                print(f"{aliados[i]} tem {vida_aliados[i]} de vida")
        
        if escolha_alvo == 2:
            vida_aliados[1]+= 5
            for i in range(len(aliados)):
                print(f"{aliados[i]} tem {vida_aliados[i]} de vida")

    if vida_inimigos[1]<=0: #Condicao para vitoria do jogador 1
        print("JOGADOR 1 VENCEU!!!")
        break



    #Vez do oponente
    print(20*"-")
    escolha=int(input(f"Escolha o numero de quem ira atacar: \n[1]. Feiticeiro\n[2]. Imperador\n[3]. Bruxo\n"))
    print(20*"-")
    

    if escolha == 1:#Feiticeiro Bate
        
        escolha_alvo=int(input(f"Escolha o numero de quem voce quer atacar \n[1]. Mago \n[2]. Rei \n[3]. Curandeiro \n "))
        print(20*"-")
        
        if escolha_alvo == 1:
            vida_aliados[0] -= 5
            for i in range(len(aliados)):
                print(f"{aliados[i]} tem {vida_aliados[i]} de vida")
        
        if escolha_alvo == 2:
            vida_aliados[1] -= 5
            for i in range(len(aliados)):
                print(f"{aliados[i]} tem {vida_aliados[i]} de vida")
        
        if escolha_alvo == 3:
            vida_aliados[2] -= 5
            for i in range(len(aliados)):
                print(f"{aliados[i]} tem {vida_aliados[i]} de vida")
       

    if escolha == 2: #Rei Bate
        
        escolha_alvo=int(input(f"Escolha o numero de quem voce quer atacar \n[1]. Mago \n[2]. Rei \n[3]. Curandeiro \n "))
        print(20*"-")
        
        if escolha_alvo == 1:
            vida_aliados[0] -= 3
            for i in range(len(aliados)):
                print(f"{aliados[i]} tem {vida_aliados[i]} de vida")
        
        if escolha_alvo == 2:
            vida_aliados[1] -= 3
            for i in range(len(aliados)):
                print(f"{aliados[i]} tem {vida_aliados[i]} de vida")
        
        if escolha_alvo == 3:
            vida_aliados[2] -= 3
            for i in range(len(aliados)):
                print(f"{aliados[i]} tem {vida_aliados[i]} de vida")
    
    
    
    if escolha == 3: #Bruxo Cura
        escolha_alvo=int(input(f"Escolha o numero de quem voce quer atacar \n[1]. Feiticeiro \n[2]. Imperador\n "))
        
        if escolha_alvo == 1:
            vida_inimigos[0] += 5
            for i in range(len(inimigos)):
                print(f"{inimigos[i]} tem {vida_inimigos[i]} de vida")

        if escolha_alvo == 2:
            vida_inimigos[1] += 5
            for i in range(len(inimigos)):
                print(f"{inimigos[i]} tem {vida_inimigos[i]} de vida")


    if vida_aliados[1]<=0: #Condicao para vitoria do jogador 2
        print("JOGADOR 2 VENCEU!!!")
        break
    