
print('Programa esta em execução')

nome = (input('infome seu nome: '))

materia = (input('infome a materia: '))

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terceira nota:'))
nota4 = float(input('Quarta nota:'))

media = (nota1+nota2+nota3+nota4)/4


if media >= 7:
    print(nome, 'Sua media foi: ', media, 'você Passou na materia:', materia)
else:
    print(nome, 'Sua media foi: ', media,
          'você não Passou na materia:', materia)
