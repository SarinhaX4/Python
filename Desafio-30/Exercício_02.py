import os

print("Descubra seu IMC:")

Kg = float(input("Qual seu peso?"))
h = float(input("Qual a sua altura?"))

resp = Kg/(h*h)

if (resp < 18.5):
    print("Magreza!")
elif (resp >= 18.5 <= 24.9):
    print("Normal")
elif (resp >= 25 <= 29.9):
    print("Sobrepeso!")
elif resp >= 30 <= 39.9:
    print("Obesidade!")
else:
   print("Obesidade grave!")

os.system("pause")