Speed = int(input('Qual sua Velocidade?'))

if Speed > 110:
    print('Sua Multa tem o valor de R$' + str( (Speed -110)*5))
else:
    print('Dentro do limite')
