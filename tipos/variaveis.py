a = 3
b = 4.4

print (a + b)

texto = 'Sua idade eh...'
idade = 23

print(texto, idade)
print(texto + str(idade))
print(f'{texto} {idade}')

saudacao = 'bom dia '
print(3 * saudacao)

#contantes (convencao usar maiusculas)
PI = 3.14
R = float(input('Informe o raio da circunferencia: '))

print(f'A circunferencia tem comprimento {2 * PI * R}')
print(f'O circulo cujo raio eh { R } tem area de { PI * R * R }')
print(f'O circulo cujo raio eh { R } tem area de { PI * R ** 2 }')
print(f'O circulo cujo raio eh { R } tem area de { PI * pow(R, 2) }')

