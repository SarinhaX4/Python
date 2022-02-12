import os

print("Cadastro de produto")

Nome = input("Nome do produto:")
Código = input("Código do produto:")
Preço =  int(input("Preço do produto:"))
Quantidade = int(input("Quantidade de produtos:"))

resp = Preço*Quantidade

print("informações sobre o produto:")
print("Nome:", Nome)
print("Código:",Código)
print("Preço:", Preço,"reais")
print("Quantidade:", Quantidade)
print("Total----------------------")
print("Total:",resp, "reais")

os.system("pause")