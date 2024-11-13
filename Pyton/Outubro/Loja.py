import os

jogos = [{"numero":1,"nome":"LOL DELUXE", "genero":"MOBA","preco":40.99,"estoque":7},
{"numero":2,"nome":"RDR 4", "genero":"Aventura","preco":579.98, "estoque":8},
{"numero":3,"nome":"Minecraft 2", "genero":"Triangulo-Retangulo","preco":199.99, "estoque":6},
{"numero":4,"nome":"Free Fire","genero":"Battle Royale","preco":0.30,"estoque":50}
]

def main():       
    """Exibe o titulo opcoes e escolhas"""
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

def exibir_titulo(titulo=""):
    """Exibe o titulo da loja na tela do usuario"""
    os.system("cls")
    print('''
████████████████████████████████████████████████████▀███████████████████████████
█▄─▄▄▀█▄─▄█─▄▄▄─██▀▄─██▄─▄▄▀█▄─▄▄▀██▀▄─██─▄▄─███─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█─▄▄▄▄█
██─▄─▄██─██─███▀██─▀─███─▄─▄██─██─██─▀─██─██─███─██▄─██─▀─███─█▄█─███─▄█▀█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀''')
    if titulo != "":
        print(f"\n{titulo}\n")

def exibir_opcoes():
    """Exibe as opcoes de acesso ao usuario"""
    print('''
1. Mostrar Jogos
2. Alterar Estoque
3. Cadastrar Jogo
4. Vender Jogos
5. Sair
''')
    
def mostrar_jogos():
    """Mostra a lista de jogos e os dados dele ao usario"""
    exibir_titulo("Lista de jogos:")
    for jogo in jogos:
        numero_jogo=jogo["numero"]
        nome_jogo = jogo["nome"]
        genero = jogo["genero"]
        preco = jogo["preco"]
        estoque = jogo["estoque"]
        print(f"{numero_jogo} | {nome_jogo} | {genero} | {preco} | {estoque}")

def escolher_opcao():
        """Permite ao usuario escolher o que ele quer acessar"""
    # try:
        escolha_usuario = int(input("Escolha uma opção do menu: "))
        if escolha_usuario == 1:
            mostrar_jogos()
            voltar_ao_menu()
        elif escolha_usuario == 2:
            mostrar_jogos()
            nome_jogo = int(input("\nQual o numero do jogo que voce deseja modificar"))
            for jogo in jogos:
                if nome_jogo == jogo["numero"]:
                    estoque = input(f"Qual é o novo valor de estoque? (Atual:{jogo["estoque"]})")
                    jogo["estoque"] = int(estoque)
                    print(f"{jogo['numero']} | {jogo["nome"]} | {jogo["genero"]} | {jogo["preco"]} | {jogo["estoque"]}")
            voltar_ao_menu()
        elif escolha_usuario == 3:
            print("Você escolheu Cadastrar Jogo")
            mostrar_jogos()
            cadastar_jogo()
            voltar_ao_menu()
        elif escolha_usuario == 4:
            mostrar_jogos()
            vender_jogo()
            voltar_ao_menu()
        elif escolha_usuario == 5:
            exibir_titulo("Você saiu do programa.")
        else:
            print("Opção Inválida")
            voltar_ao_menu()

    # except:
    #     print("Opção Inválida")
    #     voltar_ao_menu()

def voltar_ao_menu():
    """Volta ao menu"""
    input("\nAperte Enter para voltar ao menu principal.")
    main()

def cadastar_jogo():
    """Pede os dados do jogos para cadastra-los na loja"""
    numero_do_jogo=int(input("Digite em qual numero voce deseja cadastrar o jogo? "))
    nome_do_jogo=input("qual o nome do jogo que voce quer cadastrar? ")
    genero=input("digite o gênero do jogo ")
    preço=float(input("digite o preço do jogo "))
    estoque=input("digite a quantidade de jogos ")
    #  --------------------------dicionario---------------------------------#
    dados_do_jogo={"numero":numero_do_jogo, 
                    "nome":nome_do_jogo,
                   "genero":genero,
                   "preco":preço,
                   "estoque":estoque
                     }
    jogos.append(dados_do_jogo)

def vender_jogo():
    """Vende um jogo removendo uma unidade do"""
    vender=int(input("qual jogo você vai vender? "))
    jogo_indisponivel=0
    for jogo in jogos:
        if vender == jogo["numero"]:
            jogo_indisponivel=1
            jogo["estoque"]-=1
    if jogo_indisponivel==0:
        print("Opção Inválida")
        voltar_ao_menu()
        

#input()


if __name__ == '__main__':
    main()