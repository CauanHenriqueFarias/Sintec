# n_1=float(input("Qual a sua nota do primeiro trimestre?: "))
# n_2=float(input("Qual a sua nota do segundo trimestre?: "))
# n_3=float(input("Qual a sua nota do terceiro trimestre?: "))
# media=(n_1+n_2+n_3)/3
# print(f"a sua media foi {media:.2f}")

# faltas=int(input("Quantas faltas voce teve?: "))

# if media>=60 and faltas<250:
#     print("Voce foi aprovado")
# if media <60 and  media >40 and faltas<250:
#     print("Voce esta em recuperacao")
#     media_2=float(input("Qual foi a sua nota de recuperacao?: "))
#     if media_2 >=60:
#         print("Voce foi aprovado")
#     else:
#         print("Voce foi reprovado")
# if media <40 or faltas>=250:
#     print("Voce foi reprovado")


# n_1=float(input("Qual a sua nota do primeiro trimestre?: "))
# n_2=float(input("Qual a sua nota do segundo trimestre?: "))
# n_3=float(input("Qual a sua nota do terceiro trimestre?: "))
# media=(n_1+n_2+n_3)/3
# print(f"a sua media foi {media:.2f}")

# faltas=int(input("Quantas faltas voce teve?: "))

# if media>=60 and faltas<250:
#     print("Voce foi aprovado")
# elif media <60 and  media >40 and faltas<250:
#     print("Voce esta em recuperacao")
#     media_2=float(input("Qual foi a sua nota de recuperacao?: "))
#     if media_2 >=60:
#         print("Voce foi aprovado")
#     else:
#         print("Voce foi reprovado")
# else:
#     print("Voce foi reprovado")



n_1=int(input("Digite um numero"))
n_2=int(input("Digite um numero"))
if (n_1+n_2)%2==0:
    print("seu numero e par") 
else:
    print("seu numero e impar")
