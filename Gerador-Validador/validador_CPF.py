#Validador de CPF; o usuário digita um CPF e o programa verifica se os dois últimos digitos estão corretos
print('-='*8)
print('VALIDADOR DE CPF')
print('-='*8)

cpf = input('Digite seu CPF (sem pontos e traços): ')
soma_digito1 = 0 # Digito 1 é o primeiro digito depois do traço, penultimo número do CPF
soma_digito2 = 0 # Digito 2 é o segundo digito depois do traço, último número do CPF
cpf_verificado = []
cpf_lista = []
#Colocando os numéros numa lista
for a in range(len(cpf)):
    cpf_lista += cpf[a]
#definindo o primeiro digito depois do '-'
for n, p in enumerate(range(10, 1, -1)):
    cpf_verificado += cpf[n]
    multi = int(cpf[n]) * p
    soma_digito1 += multi
verificador_digito1 = 11 - (soma_digito1 % 11)

if verificador_digito1 > 9:
    digito1 = 0
else:
    digito1 = verificador_digito1
cpf_verificado += str(digito1)
#Gerando o segundo digito
for n2, p2 in enumerate(range(11, 1, -1)):
    multi = int(cpf_verificado[n2]) * p2
    soma_digito2 += multi

verificador_digito2 = 11 - (soma_digito2 % 11)

if verificador_digito2 > 9:
    digito2 = 0
else:
    digito2 = verificador_digito2

cpf_verificado += str(digito2)
#Conferindo se o CPF dado está correto
if cpf_lista == cpf_verificado:
    print('CPF valido')
else:
    print('CPF inválido')
