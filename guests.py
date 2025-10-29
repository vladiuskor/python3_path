# Ex.1 Guests list
guests_list = ['grandfather Kolya', 'grandmother Luda', 'Nataliya']
print(f'{guests_list[0].title()} I invite you to a family dinner.')
print(f'{guests_list[1].title()} I invite you to a family dinner.')
print(f'{guests_list[2].title()} I invite you to a family dinner.')

# Ex.2 Fix guests list
print(f'{guests_list[-1].title()} cant go to dinner.')
guests_list[-1] = 'grandfather Borya'
print(guests_list)
print(f'{guests_list[0].title()} I invite you to a family dinner.')
print(f'{guests_list[1].title()} I invite you to a family dinner.')
print(f'{guests_list[2].title()} I invite you to a family dinner.')

# Ex.3 More guests
print('We can invite more guests to our dinner!!!')
guests_list.insert(0, 'mother')
guests_list.insert(2, 'grandmother Luba')
guests_list.append('filip')

print(f'{guests_list[0].title()} I invite you to a family dinner.')
print(f'{guests_list[1].title()} I invite you to a family dinner.')
print(f'{guests_list[2].title()} I invite you to a family dinner.')
print(f'{guests_list[3].title()} I invite you to a family dinner.')
print(f'{guests_list[4].title()} I invite you to a family dinner.')
print(f'{guests_list[5].title()} I invite you to a family dinner.')

# Ex.4 Trouble with table
print("Our table can't be brought on time, so we need to reduce the number of guests to two people.")
print(f'{guests_list.pop().title()}, We are very sorry about the cancellation of the invitation.')
print(f'{guests_list.pop().title()}, We are very sorry about the cancellation of the invitation.')
print(f'{guests_list.pop().title()}, We are very sorry about the cancellation of the invitation.')
print(f'{guests_list.pop().title()}, We are very sorry about the cancellation of the invitation.')

print(f'Dear {guests_list[0].title()}, the invitation remains valid.')
print(f'Dear {guests_list[1].title()}, the invitation remains valid.')

del guests_list[0]
del guests_list[0]
print(guests_list)
