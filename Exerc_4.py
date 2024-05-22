algo = input("Digite algo: ")
print("O que você digitou é ", type(algo))

print(algo, "É somente espaços, ou seja, valores em branco? ", algo.isspace())
print(algo, "É um número?? ", algo.isnumeric())
print(algo, "Está em maiúsculas? ", algo.isupper())
print(algo, "Está em minúsculas? ", algo.islower())
print(algo, "Está capitalizado? ", algo.istitle())