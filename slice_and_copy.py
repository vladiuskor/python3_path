# Ex.1 Slices
drug_names = [
    "paracetamol",
    "ibuprofen",
    "amoxicillin",
    "metformin",
    "atorvastatin",
    "omeprazole",
    "losartan",
    "cetirizine",
    "azithromycin",
    "sertraline"
]

drug_names_middle_item = int(len(drug_names) / 2 - 1)
print(drug_names_middle_item)

print(f"The first three items in the list are:{drug_names[:3]}")
print(f"Three items from the middle of the list are:{drug_names[drug_names_middle_item : drug_names_middle_item + 3]}")
print(f"The last three items in the list are:{drug_names[-3:]}")
print('\n')

# Ex.2 Pizzas
my_pizzas = ['Salami', 'Tonno', 'Ham', 'Margherita', 'Hawaii', 'Quattro formaggi', 'Funghi']
friend_pizzas = my_pizzas[:]

print(f'My pizzas before:{my_pizzas}')
print(f'My friends pizzas before:{friend_pizzas}')

print('---***---')

my_pizzas.append('Village')
friend_pizzas.append('Chezare')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)

print('\n')

print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


