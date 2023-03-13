while True:  # loop que recebe e valida o input do usuário
    try:
        num_informado = int(input("Digite um número >>> "))
        if num_informado < 0:
            raise ValueError
    except ValueError:
        print("\nO valor informado deve ser um número natural (inteiro maior ou igual a 0)!")
        continue
    else:
        break


# testando se o número informado pertence à sequência de Fibonacci

if num_informado == 0 or num_informado == 1:
    print("\nO número informado PERTENCE a sequência de Fibonacci.")
else:
    a = 0
    b = 1
    c = a + b
    while c < num_informado:
        a = b
        b = c
        c = a + b

    if c == num_informado:
        print("\nO número informado PERTENCE a sequência de Fibonacci.")
    else:
        print("\nO número informado NÃO pertence a sequência de Fibonacci.")
