"""Krotki listy elementów dla zmiennej, krotki są stałe i nie można ich modyfikować
    do tworzenia krotek służy przecinek, a nawiasy okrągłe są na ogół opcjonalne,
    każdy z elementów ma inne znaczenie
"""

pair = ('a', 2) # krotki przeważnie są w okrągłych nawiasach, argumenty mogą być róznej klasy, np. string i integer
print(f'\nto jest krotka --> {pair} zawierająca string "a" i integer 2, krotka jest klasy:  {type(pair)}\n')

pair = 'a', 2
print(f'to też jest krotka --> {pair} zawierająca string "a" i integer 2, krotka jest klasy:  {type(pair)}\n')

empty = ()
print(f'to jest pusta krotka --> {empty}\n')


# Krotka jednoelementowa

one_elem_tuple = ('a',) # trzeba pamiętać o dodaniu przecinka po argumencie
print(f'to jest krotka jednoelementowa --> {one_elem_tuple} zawierająca tylo string "a", krotka jest klasy:  {type(one_elem_tuple)}\n')

one_elem_tuple = 'a', # przecinek po argumencie tworzy krotkę
print(f'to też jest krotka jednoelementowa --> {one_elem_tuple} zawierająca tylo string "a", krotka jest klasy:  {type(one_elem_tuple)}\n')


# Krotka nie jest modyfikowalna, nie można jej zmienić

my_tuple = ('a', 'b', 'c')
sec_tuple_item = my_tuple[1] # elementy krotki pobieramy jak elementy listy
print(f'to jest drugi element krotki --> {sec_tuple_item}\n')

new_sec_tuple_item = 'change'
print(f'gdy chcemy podmienić: {sec_tuple_item} na {new_sec_tuple_item} to nam się nie uda\n')
my_tuple[1] = new_sec_tuple_item # TypeError: 'tuple' object does not support item assignment