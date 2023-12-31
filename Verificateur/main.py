from functions.regex_functions import *
from functions.read_jupyter import *

import os
os.chdir("Verificateur")


liste_functions_text_cell = [
    check_pep8,
    check_abreviation,
    check_separation,
    check_final_space,
    check_first_initial,
    check_function_name,
    check_largeur,
    count_ligne_function,
    count_ligne_cell,
    count_parametre,
    nested_function,
    check_espaces,
    check_branchement_successifs
]

log_text = check_naming()

file_name = "pile_file"
dico_ipynb = read_ipynb(file_name)
liste_cellule_code = make_liste_cell(dico_ipynb)

text_cell = liste_cellule_code[0]
for text_cell in liste_cellule_code:
    if len(text_cell)>0 and text_cell[0] != "#":
        for function_regex in liste_functions_text_cell:
            log_text += "," + function_regex(text_cell)

liste_code = log_text.split(",")
set_code = set(liste_code)
liste_code = list(set_code)
liste_code.remove("")
if len(liste_code)>0:
    log_text = ",".join(liste_code)
    print("--------------------------------")
    print(log_text)
    with open("error.txt","w+") as file:
        file.write(log_text)
else:
    print("Pas d'erreur")
