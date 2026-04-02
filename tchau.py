minu = int(input('tempo em minutos: '))

if minu < 200:
    print(minu*0.20)
elif minu >= 200 and minu < 400:
    print(minu * 0.18)
else:
    print(minu * 0.15)
