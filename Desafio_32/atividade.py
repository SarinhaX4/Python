import os 

print("Multiplique seus números aqui")
def multiplicacao(n1,n2):
    print(n1,"x", n2, "=", n1*n2)

resp1 = int(input("Digíte um número:"))
resp2 = int(input("Digite outro número:"))

multiplicacao(resp1,resp2)

os.system("pause")