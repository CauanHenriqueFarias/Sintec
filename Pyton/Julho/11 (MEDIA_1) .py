n_1=float(input("Qual a sua nota do primeiro trimestre?: "))
n_2=float(input("Qual a sua nota do segundo trimestre?: "))
n_3=float(input("Qual a sua nota do terceiro trimestre?: "))
media=(n_1+n_2+n_3)/3
print(f"a sua media foi {media:.2f}")

faltas=int(input("Quantas faltas voce tem?: "))


if (media <60) or (faltas>=250):
    print("REPROVADO!!!")
else:
    print("Parabens! Voce foi aprovado!")
