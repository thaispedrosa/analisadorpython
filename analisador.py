somaidade = 0
mediaidade=0
maioridadehomem=0
nomemaisvelho=''
totmulher20=0
for i in range (1,5):
    print('------- {}* PESSOA --------'.format(i))
    nome=str(input('Nome:')).strip()
    idade=int(input('Idade:'))
    sexo=str(input('Sexo [M/F]:')).strip()

    somaidade += idade

    if i ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho=nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho=nome
    if sexo in 'Ff' and idade> 20:
        totmulher20 +=1


mediaidade = int(somaidade/4)
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomemaisvelho))
print('Ao todo de {} mulher(es) com menos de 20 anos.'.format(totmulher20))