def main():

    #Usuario digita as notas
    nota1 = input("Digite a primeira nota:")
    nota2 = input("Digite a segunda nota:")
    nota3 = input("Digite a terceira nota:")
    nota4 = input("Digite a quarta nota:")

    #strings guardam inteiros
    nota1_int = int (nota1)
    nota2_int = int (nota2)
    nota3_int = int (nota3)
    nota4_int = int (nota4)
 

    #calcule a media das notas
    notafinal = (nota1_int + nota2_int + nota3_int + nota4_int)/4
    

    #imprima a media das notas
    print("A média aritmética é",notafinal)

main()
    
