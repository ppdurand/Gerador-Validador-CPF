from random import randint 

print('-='*7)
print('GERADOR DE CPF')
print('-='*7)

numero = str(randint(100000000, 999999999))
cpf = numero
soma_digito1 = 0
soma_digito2 = 0
novo_cpf = []
cpf_lista = []
new = 0
#Colocando o CPF numa lista para facilitar o iteiramento
for a in range(len(cpf)):
    cpf_lista += cpf[a]
#definindo o primeiro digito depois do '-'
for n, p in enumerate(range(10, 1, -1)):
    novo_cpf += cpf[n]
    multi = int(cpf[n]) * p
    soma_digito1 += multi

verificador_digito1 = 11 - (soma_digito1 % 11)

if verificador_digito1 > 9:
    digito1 = 0
else:
    digito1 = verificador_digito1
novo_cpf += str(digito1)
#Definindo o segundo dígito
for n2, p2 in enumerate(range(11, 1, -1)):
    multi = int(novo_cpf[n2]) * p2
    soma_digito2 += multi

verificador_digito2 = 11 - (soma_digito2 % 11)

if verificador_digito2 > 9:
    digito2 = 0
else:
    digito2 = verificador_digito2

novo_cpf += str(digito2)
#Mostrar o CPF gerado
for z in range(len(novo_cpf)):
    print(novo_cpf[z], end='')

