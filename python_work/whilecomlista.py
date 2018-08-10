#Começa com os usuarios que precisam ser verificados,
#e com uma lista vazia para armazenar os usuarios confimados
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifica cada usuario ate que nao haja mais usuarios nao confirmados
# Transfere cada usuario verificado para a lista de usuarios confirmados
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Exibe todos os usuarios confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

