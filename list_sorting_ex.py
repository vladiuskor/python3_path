# Ex.1
countries = ['Poland', 'Italy', 'England', 'Norway', 'Sweden', 'Spain', 'Czechia']
countries_list = " ".join(countries).lower().split(' ')

print(f'Countries where I want to go: {countries_list}')
print(f'Sorted countries list: {sorted(countries_list)}')

print(f'\nCountries where I want to go one more time: {countries_list}')
print(f'Reverse sorted countries list: {sorted(countries_list, reverse=True)}')
print(f'\nCountries where I want to go one more time: {countries_list}')

countries_list.reverse()
print(f'\nReversed string: {countries_list}')
countries_list.reverse()
print(f'Reversed string: {countries_list}')

countries_list.sort()
print(f'\nCountries where I want to go (sort): {countries_list}')
countries_list.sort(reverse=True)
print(f'\nCountries where I want to go (sort and reverse): {countries_list}')

# Ex.2
print(f'\nI want to visit {len(countries_list)} countries!')



