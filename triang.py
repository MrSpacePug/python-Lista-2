la = int(input("lado 1 do triangulo"))
lb = int(input("lado 2 do triangulo"))
lc = int(input("lado 3 do triangulo"))

if la + lb > lc:
    if la + lc > lb:
        if lc + lb > la:
            print('Valido')
else:
    print('invalido')

if la == lb == lc:
    print('Triangulo Equilatero')
elif la != lb != lc:
    print('Triangulo Escaleno')
else:
    print('Triangulo Isósceles')
