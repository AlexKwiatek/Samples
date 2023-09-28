import glob
import os
import re
import random

file_list = glob.glob(os.path.join(os.getcwd(), "cultures", "*.txt"))

corpus = []

for file_path in file_list:
    with open(file_path) as f_input:
        corpus.append(f_input.read())

corpus = [y.split('\n') for y in corpus]

list_of_cultures = []
their_namelists = []
for file in corpus:
    for x in file:
        if not "\t" in x and "{" in x:
            processed = x.split(" ")[0]
            list_of_cultures.append(processed)
        elif "name_list" in x:
            processed = x.split(" ")[-1]
            their_namelists.append(processed)

culture_and_namelist_dict = dict(zip(list_of_cultures,their_namelists))

### And now the same for lists

# Ustal ścieżkę do folderu "name_lists"

file_list = glob.glob(os.path.join(os.getcwd(), "name_lists", "*.txt"))

# Lista na wynik
results = []

# Przetwarzaj każdy plik
for file_path in file_list:
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    # Użyj wyrażenia regularnego do wyodrębnienia bloków name_list
    name_list_blocks = re.findall(r'name_list_([^\s]+)\s*=\s*{\s*(.*?)^\s*}\s*}', file_contents, re.DOTALL | re.MULTILINE)

    # Przetwarzaj każdy blok
    for block_name, block_content in name_list_blocks:
        # Wyodrębnij imiona męskie
        male_names = re.findall(r'male_names\s*=\s*{\s*([^}]+?)}', block_content, re.DOTALL)
        male_names = [name.strip() for name in male_names[0].split('\n') if name.strip()]

        # Wyodrębnij imiona żeńskie
        female_names = re.findall(r'female_names\s*=\s*{\s*([^}]+?)}', block_content, re.DOTALL)
        #print(female_names[0])
        female_names = [name.strip() for name in female_names[0].split('\n') if name.strip()]

        # Dodaj wynik do listy wynikowej
        results.append([f"name_list_{block_name}", male_names, female_names])


list_of_namelists = []
for result in results:
    output_list = []
    # Przechodzimy przez każdy element w wejściowej liście
    for item in result:
        # Jeśli element jest listą i ma więcej niż jeden element
        if isinstance(item, list) and len(item) > 1:
            # Podziel każdy element na osobne słowa, rozdzielając po spacji
            split_words = [word.split() for word in item]
            # Połącz słowa w jedną listę
            flattened_words = [word for sublist in split_words for word in sublist]
            output_list.append(flattened_words)
        else:
            output_list.append(item)
    list_of_namelists.append(output_list)

# Inicjalizacja pustego słownika
namelist_dict = {}

# Iteracja przez każdą listę w wejściowej liście
for item in list_of_namelists:
    # Sprawdzenie, czy lista ma przynajmniej trzy elementy
    if len(item) >= 3:
        # Pierwszy element jako klucz, a drugi i trzeci jako wartość w słowniku
        key = item[0]
        value = [item[1], item[2]]
        namelist_dict[key] = value

def get_random_name(culture,female):
    return random.choice(namelist_dict[culture_and_namelist_dict[culture]][female])
