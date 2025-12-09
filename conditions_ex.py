# Ex. 1 Check conditions
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

warrior_data = {
    "firstname": "Vlad",
    "lastname": "Ko",
    "sex": "male",
    "born": "1995",
    "country": "Ukraine",
    "served": "no",
}

print(f"Your firstname is Vlad. {warrior_data["firstname"] == "Vlad"}")
print(f"Your firstname is Petro. {warrior_data["firstname"] == "Petro"}")
print(f"Your lastname is Ko. {warrior_data["lastname"] == "Ko"}")
print(f"Your lastname is Lo. {warrior_data["lastname"] == "Lo"}")
print(f"Your sex is male. {warrior_data["sex"] == "male"}")
print(f"Your sex is female. {warrior_data["sex"] == "female"}")

print('\n ******** \n')

# Ex. 2
random_name_1 = 'Chico'
random_name_2 = 'Lola'

random_number_1 = 77
random_number_2 = 12

random_list = ['stone', 'wood', 'iron', 'water', 'air']

print(random_name_1 == 'Chico')
print(random_name_1 == random_name_2)
print(random_name_2.lower() == 'Lola')
print(random_name_2.lower() == 'lola'.lower())

print('******')

print(random_number_1 > 45)
print(random_number_2 > 45)
print(random_number_1 <= 77)
print(random_number_2 >= 12)

print('******')

print(random_number_1 > 40 and random_number_2 > 13)
print(random_number_1 > 45 or random_number_2 > 13)

print('******')

print('water' in random_list)
print('plasma' in random_list)

if 'plasma' not in random_list:
    print('plasma is not found in this list.')