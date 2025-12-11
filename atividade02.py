# Calcular o IMC
# 1 - Inserir altura e peso de uma ou mais pessoas
# 2 - classificação correspondente de cada pessoa, com base no resultado do cálculo do IMC. 
# Menor que 16,9 muito abaixo do peso


def calcula_imc(p, a):
    imc = peso/(p * a )
    return imc




peso = float(input('Informe seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = calcula_imc(altura, peso)


match imc:
    case imc if imc <= 16.9:
        print('Muito abaixo do peso')
    case imc if imc <= 18.4:
        print('Abaixo do peixe')
    case imc if imc <= 24.9:
        print('peso normal')
    case imc if imc <= 24.9:
        print('peso normal')
    case imc if imc <= 34.9:
        print('Obesidade grau I')
    case imc if imc <= 40:
        print('Obesidade grau II')
    case imc if imc > 40:
        print('Obesidade grau III')
        

    

    
