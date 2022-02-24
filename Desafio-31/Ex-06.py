import os

n = int(input("digíte um número:"))

for x in range(1,n):
    if x%2 == 1:
        print(x)

os.system("pause")