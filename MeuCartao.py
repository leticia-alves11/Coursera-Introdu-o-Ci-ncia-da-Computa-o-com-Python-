meuCartao = int(input("Digite o número do seu cartão de crédito:"))

cartaoLido = 1
encontreiMeuCartaonalista = False


while cartaoLido != 0 and not encontreiMeuCartaonalista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito:"))

    if cartaoLido == meuCartao:
        encontreiMeuCartaonalista = True

if encontreiMeuCartaonalista:
    print("Encontrei meu cartão!")

else:
    print("Não localizei meu cartão!")
