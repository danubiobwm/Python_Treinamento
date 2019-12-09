import random 

num_secreto=random.randint(95, 100) #ultimo numero pertence ao sorteio

num=int(input('digite seu numero: '))

if num_secreto == num:
  print('você ganhou')
else:
  print('vc não ganhou')
