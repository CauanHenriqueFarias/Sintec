presentes=[]
num_presentes=int(input("Qual a quantidade de presentes?: "))
print(20*"-")

for i in range(num_presentes):
    presentes.append(input(f"{i+1}-Qual o presente?: ").strip().title())

print(20*"-")
print("LISTA DOS PRESENTES.")
for i in range(len(presentes)):
    print(f"{i+1}-{presentes[i]}")

resposta=input("Voce deseja que algum item seja removido?:").strip().title()

if resposta == "Sim":
    presentes.remove(str(input("Qual o item que voce seja excluir?: ").strip().title()))

print(20*"-")
print("LISTA DOS PRESENTES.")
for i in range(len(presentes)):
    print(f"{i+1}-{presentes[i]}")


