num_inteiro = int(input("Digite um número inteiro:"))

soma = 0

while num_inteiro != 0:
    soma = soma+(num_inteiro % 10)
    num_inteiro = num_inteiro//10

print(soma)
