'''
a program that shows how to create n empty <class 'list'> lists
in the <class 'list'> element
'''
import os, json

root_path = os.getcwd()
output = 'output'
json_ext = 'json'
utf_8 = 'UTF-8'

'''
variable containing data in json format

zmienna zawierająca dane w formacie json
'''
data = {"entries": \
            [\
                {"attributes": {"test" : "json", "test1":"saved"}, "dn": "CN=Group-rw,OU=Groups,OU=UNIVERSUM,DC=universum,DC=local"}, \
                {"attributes": {"test" : "json", "test1":"saved"}, "dn": "CN=Computer-01,OU=Computers,OU=UNIVERSUM,DC=universum,DC=local"}, \
                {"attributes": {"test" : "json", "test1":"saved"}, "dn": "CN=User-01,OU=Users,OU=UNIVERSUM,DC=universum,DC=local"}\
            ]\
        }

'''
entry to the json file, to the list of entries

wejście do pliku json, do listy entries
'''
retrived_accounts_list = data['entries']

'''
<class 'list'> variable containing string <class 'str'> elements

zmienna <class 'list'> zawierajaca elementy string <class 'str'>
'''
output_file_names = ['01_file_users', '02_file_computers', '03_file_groups']

'''
variable - new empty list <class 'list'> to enter data

zmienna - nowa pusta lista <class 'list'> do wpisania danych
'''
fnames = []

'''
a for loop that reads the items from the output_file_names list
one by one and writes them in to the list of fnames

petla for odczytujaca kolejno elementy z listy output_file_names i wpisująca je
do listy fnames
'''
for fname in output_file_names:
    '''
    the append() function writes to an empty list
    subsequent fname elements, adding additional ones
    data from variables

    funkcja append() wpisuje do pustej listy
    kolejne elementy fname, dodając dodatkowe
    dane ze zmiennych
    '''
    fnames.append(f'{root_path}/{output}/{fname}.{json_ext}')

'''
variable <class 'list'> inside which empty lists [] are created
in the number equal to the number of elements in the list fname

zmienna <class 'list'> w której wętrzu tworzone są puste listy []
w liczbie równej ilości elementów wewnątrz listy fname
'''
json_dics = [[] for _ in range(len(fnames))]

'''
a for loop that searches the data from the data variable
and writes them to the appropriate, previously created lists

pętla for która przeszukuje dane ze zmiennej data
i zapisuje je odpowiednich, wcześniej utworzonych list
'''
for account in retrived_accounts_list:
    dn = account['dn']
    attributes = account['attributes']
    if 'OU=Users,OU=UNIVERSUM,DC=universum,DC=local' in str(dn):
        json_dics[0].append({ "new-test": attributes['test'], "new-test1": attributes['test1'], "dn": dn })
    if 'OU=Computers,OU=UNIVERSUM,DC=universum,DC=local' in str(dn):
        json_dics[1].append({ "new-test": attributes['test'], "new-test1": attributes['test1'], "dn": dn })
    if 'OU=Groups,OU=UNIVERSUM,DC=universum,DC=local' in str(dn):
        json_dics[2].append({ "new-test": attributes['test'], "new-test1": attributes['test1'], "dn": dn })


'''
a function that writes data to a json file
funkcja, która zapisuje dane do pliku json
'''
def save_to_json(json_dic, data_to_save):
    with open(data_to_save, 'w', encoding= utf_8) as json_file:
        json.dump(json_dic, json_file, ensure_ascii= False, indent=4, sort_keys= True)


'''
for loop, which, using the save_to_json() function,
creates as many files as there are elements in the fnames list,
allocating files from the fnames list to the lists created accordingly
in the for account in retrived_accounts_list loop

pętla for, która przy wykorzystaniu funkcji save_to_json() tworzy tyle plików
ile jest elementów w liście fnames przydzielając odpowiednio utworzonym listom
w pętli for account in retrived_accounts_list pliki z listy fnames
'''
for i in range(len(fnames)):
    save_to_json(json_dics[i], fnames[i])
