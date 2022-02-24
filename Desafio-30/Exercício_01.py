import os

print("Descubra se você foi APROVADO ou REPROVADO -----------")
print("Digite:")

n1 = float(input("Sua primeira nota:"))
n2 = float(input("Sua segunda nota:"))
n3 = float(input("Sua terceira nota:"))

resp = (n1+n2+n3)/3

print("--------------------")

print(n1,"+",n2,"+",n3,"/","3","=",resp)

if resp < 6:
    print(" Você foi reprovado!")
else:
    print("Parabéns! Você foi aprovado!")
    

os.system("pause")