alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

#Consultar quantos pontos um jogador ganha por atingir um alienigena
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#Adicionando novos pares chave-valor
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Modificando valores em um dicionario
print("The alien is " + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')

#Movendo o alienigena para a direita
#Determina a distancia que o alienigena deve se deslocar de acordo com sua velocidade atual
alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #Este deve ser um alienigena rapido
    x_increment = 3

#A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#Removendo pares chave-valor
del alien_0['points']
print(alien_0)

#Percorrendo todos os pares chave-valor com um laço
user_0 = {'username': 'efermi',
          'first' : 'enrico',
          'last' : 'fermi'}

for key, value in user_0.items():           #Para receber só a chave usasse user_0.keys() e user_0.values() para o valor
    print("\nKey: " + key)
    print("Value: " + value)

#Criando lista de alienigenas
aliens = []
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

#Mostra os 5 primeiros alienigenas
for alien in aliens[:5]:
    print(alien)
print("...")

#Mostra quantos alienigenas foram criados
print("Total number of aliens: " + str(len(aliens)))