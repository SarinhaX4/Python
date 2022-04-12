from cgitb import text
import os

nome = "texto.txt"
cont = 0

if os.path.exists(nome):
    arquivo = open(nome, "r")
    texto = arquivo.read()
    
    for x in range(len(texto)):
        if text:
            texto[x] == "a" or texto[x] == "A"
            texto[x] == "e" or texto[x] == "E"
            texto[x] == "i" or texto[x] == "I"
            texto[x] == "o" or texto[x] == "O"
            texto[x] == "U" or texto[x] == "U"
        
            cont += 1
    print("A quantidade de vogais é:", cont)
else:
    print("O arquivo não foi encontrado!")

os.system("pause")