players = ['Vlad', 'Olenka', 'Olexander', 'Roma', 'Dima']
print(players[0:3])
print(players[1:])
print(players[-2:])

print('\n')

new_players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Here are the first three players on my team:')
for player in new_players[:3]:
    print(player.title())
