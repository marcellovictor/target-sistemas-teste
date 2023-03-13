string = str(input("Digite algo >>> "))
print(f"\nVocê digitou: {string}")

i = 0

string = list(string)

while i < len(string)/2:
    aux = string[i]
    string[i] = string[len(string)-i-1]
    string[len(string)-i-1] = aux

    i += 1

string = "".join(string)

print(f"\nString invertida: {string}\n")


"""
Em python, poderia ter feito apenas string = string[::-1], mas novamente, por se tratar
de uma avaliação independente de linguagem, resolvi fazer de forma mais genérica.
"""