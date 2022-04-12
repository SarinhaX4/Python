import os
print("A fim de se lembrar de todos os animais vistos no zoológico, adicione á lista os animais que visitar.")
lista = ["tamandua", "tigre", "cobra", "elefante", "girafa"]
print(lista)

nome = input("Adicione um animal:")
lista.append(nome)
print(lista)

os.system("pause")