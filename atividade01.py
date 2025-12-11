# Regulamento do estado - quantidade máxima permitida por dia 100 quilos
# Caso ultrapasse 100 quilos, paga multa de 4 reais por excedente
# requisito
# 1 - Receber o peso total de peixes pescados por dia
# 2 - Verifique se houve excesso
# 3 - Calcule e retorne o valor da multa, se houver
# 4 - Mostre a mensagem correspondente na tela


# def calcular_multa(peso, multa):
    
    


# total_dia = float(input('Informe o peso total permitido: '))   # ESTOU FAZENDO ESSE DE VERDE
# peso = float(input('Informe o peso total do dia: '))
# multa = float(input('informe o valor da multa: '))
# print(f'O total do peso é {peso}')

# if peso >= 100:
#     print('Seguir')
# else:
#     print('pagar a multa') 

# ---------------------------------------------------CORREÇÃO DO PROFESSOR

def calcular_multa(excesso):
    multa = excesso * MULTA_KG
    return multa


MULTA_KG = 4.00
QUILO_PERMITIDOS = 100.0   # caso mude esse kg em algum momento eu consigo alterar em qq momento, que conseguirei ter o resultado

peso_pescado = float(input('Informe o peso: '))

if peso_pescado > QUILO_PERMITIDOS:
    excedente =  peso_pescado - QUILO_PERMITIDOS      # esse vai pra cima na parte def
    vl_multa = calcular_multa(excedente)
    print(f'O valor da multa é {vl_multa}')
else:
    print('Não há multa a pagar! ')

print('Programa encerrado! ')















