"""Listy = uporządkowana tablica od 0 dla elementów mających takie samo znaczenie, np. nazwy plików czy wartości integer
"""
filenames = ['data.csv', 'another.csv', 'yet-another.csv'] # przykładowa lista zawierająca nazwy plików
print(f'\nto jest zawartość listy -->             {filenames}\n')

item_1 = filenames[0] # pierwszy element posiada indeks 0
print(f'to jest pierwszy element z listy -->    {item_1}\n')

last_item = filenames[-1] # ostatni element z listy, odlicza od końca listy
print(f'to jest ostatni element z listy -->     {last_item}\n')

i = 0 # licznik
for filename in filenames: # przy pomocy pętli for możemy wykonać te same operacje na kolejnych elementach z listy
    i += 1 # po każdym elemencie zwiększamy licznik o +1 (i=i+1)
    print(f'to jest {i} element z listy --> {filename} a jego indeks w liście = {i-1}')

"""Listy są modyfikowalne, to znaczy, że możemy zmieniać ich elementy
"""

filenames.append('dodatkowy-plik.csv') # używając metody append dodajemy do końca listy kolejny element
print(f'\nto jest nowa zawartość listy -->              {filenames}\n')

new_item_1 = 'zmiana-pliku.csv'
filenames[0]= new_item_1 # zmiana pierwszego elementu listy z data.csv na zmiana-pliku.csv
print(f'to jest nowa zawartość listy po zmianie -->   {filenames}\n')
