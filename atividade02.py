# Calcular o IMC
# 1 - Inserir altura e peso de uma ou mais pessoas
# 2 - classificação correspondente de cada pessoa, com base no resultado do cálculo do IMC. 
# Menor que 16,9 muito abaixo do peso


def calcula_imc(peso, a):
    imc = peso/(a**2)
    return imc




peso = float(input('Informe seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = calcula_imc(peso, altura)



match imc:
    case imc if imc <= 16.9:
        print('Muito abaixo do peso')
    case imc if imc <= 18.4:
        print('Abaixo do pese')
    case imc if  imc <= 24.9:
        print('peso normal')
    case imc if imc <= 29.9:
        print('peso normal')
    case imc if  imc <= 34.9:
        print('Obesidade grau I')
    case imc if imc <= 40:
        print('Obesidade grau II')
    case imc if 40 <imc:
        print('Obesidade grau III')

print(f'O seu IMC é: {imc:.2f}')
        

    

    
