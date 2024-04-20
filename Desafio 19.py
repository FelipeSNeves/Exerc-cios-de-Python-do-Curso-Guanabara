import random
a1 = str(input('Digite o primeiro maconheiro:'))
a2 = str(input('O segundo:'))
a3 = str(input('O terceiro:'))
a4 = str(input('O quarto:'))
list = [a1 , a2 , a3 , a4]
escolhido = random.choice(list)
print('O que vai botar o seu hoje é o:{}'.format(escolhido))