"""Słownik to inaczej mapa
"""

# use case

# zliczanie ile razy wystąpiło słowo 'Alice w tekście
text = 'Alice has a cat'

counter = 0 # licznik dla słowa 'Alice'
for word in text.split():
    if word == 'Alice':
        counter +=1
print(f'\nw tekście --> "{text}" słowo "Alice" wystąpiło x {counter}\n')

# tworzenie słowników
dictionary = { # słownik składa sie z wartości klucza i przypisanej do niego wartości zmiennej
    'key': 'value',
    'key2': 'value2'
    }
print(f'to jest przykładowy słownik --> {dictionary}\n')

dictionary = {
    'Alice': 3,
    'has': 1
    }
print(f'słownik --> {dictionary}\n')

dictionary['a'] = 2 # dodawanie klucza i wartości do słownika --> dictionary['key] = value
print(f'to jest nowy słownik --> {dictionary}\n')

print(f"to jest wartośc dla klucza 'Alice' w słowniku --> {dictionary['Alice']}\n") # forma odczytu słownika dla konkretnego klucza

# wypisywanie całego słownika przy pomocy pętli for
print(f'to sa kolejno wartości ze słownika:')
for key, val in dictionary.items(): # używając metody .items() pobieramy klucz i wartość do niego przypisaną 
    print(f' klucz: {key} : wartość {val}')