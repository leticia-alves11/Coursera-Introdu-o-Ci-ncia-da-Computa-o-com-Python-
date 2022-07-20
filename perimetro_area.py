def main():

    #usuario vai informar o valor do lado do quadrado e será armazenado em string
    p_str = input ("Digite o valor correspondente ao lado de um quadrado:")

    p_int = int(p_str) #converte string em inteiro

    #calculando o perimetro
    perimetro = 4*p_int
    area = p_int**2

    #imprima o valor do perimetro do quadrado
    print ("perímetro:",perimetro,"-","área:",area)

main()
