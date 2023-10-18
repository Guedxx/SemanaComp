def addcontato():
    contatos = []
    nome = input('Escreva o nome do contato:')
    numero = input('Escreva o número do contato:')
    contatos.append(nome)
    contatos.append(numero)
    return contatos

lista_contatos = []
N = 0
while N == 0:
    lista_contatos.append(addcontato())
    X = int(input('Novo contato? Sim = 1 Não = 0'))
    if x == 1:
        N += 1
    else:
        pass


print(lista_contatos)
