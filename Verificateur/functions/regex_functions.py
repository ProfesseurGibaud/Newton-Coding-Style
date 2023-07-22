import re
import os


def check_naming():
    with open("data/mot_interdits.txt","r") as file:
        liste_mots_interdits = file.read().split(",")
    for file_ in os.listdir():
        if file_.lower() != file_ :
            print("Nom de fonctions problématiques")
            return "O-2"
        if file_ in liste_mots_interdits:
            return "O-2"
    return ""  

def check_minuscule(texte):
    return not texte.lower() == texte


def check_pep8(texte_cell):
    pattern_fonction = "def (\w+)"
    pattern_variable = "(\w+) ?="
    for variable in re.findall(pattern_variable,texte_cell):
        if check_minuscule(variable):
            print(f"{variable} Pep8")
            return "O-1"
    for name_function in re.findall(pattern_fonction,texte_cell):
        if check_minuscule(name_function):
            print(f"{name_function} pep8")
            return "O-1"
    return ""   

def check_abreviation(text_cell):
    pattern_fonction = "def (\w+)"
    pattern_variable = "(\w+) ?="
    with open("data/mot_interdits.txt","r") as file:
        liste_mots_interdits = file.read().split(",")
    for item in re.findall(pattern_fonction,text_cell):
        if len(item) == 1:
            print(f"{item} abréviation")
            return "O-3"
        if item in liste_mots_interdits:
            print(f"{item} abréviation")
            return "O-3"
    for item in re.findall(pattern_variable,text_cell):
        if len(item) == 1:
            print(f"{item} abréviation")
            return "O-3"
        if item in liste_mots_interdits:
            print(f"{item} abréviation")
            return "O-3"
    return ""

def check_separation(text_cell):
    pattern_espace_avant_fonction = "[:|=](.+)def|[:|=](.+)class"
    liste_item = re.findall(pattern_espace_avant_fonction,text_cell)
    for i in range(1,len(liste_item)):
        item = liste_item[i]
        if item.count("\n") != 1:
            print(f"{item} separation")
            return "G-1"
    return ""

def check_final_space(text_cell):
    if text_cell != "":
        if text_cell[-1] == " ":
            print(f"{text_cell} final space")
            return "G-3"
    return ""

def check_first_initial(text_cell):
    if text_cell != "":
        if text_cell[0] == " ":
            print(f"{text_cell} first space")
            return "G-4"
    return ""

def check_function_name(text_cell):
    pattern_fonction = "def (\w+) ?:"
    for name_function in re.findall(pattern_fonction,text_cell):
        if name_function.count("_") == 0:
            print(f"{name_function} function name")
            return "F-2"
    return ""

def check_largeur(text_cell):
    for texte_ligne in text_cell.split("\n"):
        texte_ligne = texte_ligne.strip()
        if len(texte_ligne) > 80:
            print(f"{texte_ligne} largeur")
            return "F-3"
    return ""

def count_ligne_function(text_cell):
    pattern_function_inside = "def \w+\(.*\): ?\\n    (.*)\\n\\n"
    liste_function_inside = re.findall(pattern_function_inside,text_cell)
    for function_inside in liste_function_inside : 
        if function_inside.count("\n") >= 20:
            print(f"{function_inside} longueur")
            return "F-4"
    return ""

def count_ligne_cell(text_cell):
    pattern_function_full = "(def .+)\\n\\n"
    for function_text in re.findall(pattern_function_full,text_cell):
        text_cell = text_cell.replace(function_text,"")
    if text_cell.count("\n") >= 20:
        print(f"{text_cell} longueur")
        return "F-4"
    else:
        return ""

def count_parametre(text_cell):
    pattern_parameter = "def \w+\((.*)\)"
    for parameters_functions in re.findall(pattern_parameter,text_cell):
        if len(",".split(parameters_functions))>4:
            return "F-5"
    return ""

def nested_function(text_cell):
    pattern_function_inside = "def \w+\(.*\): ?\\n    (.*)\\n\\n"
    for function_inside in re.findall(pattern_function_inside,text_cell):
        if "def " in function_inside:
            print(f"{function_inside} nested function")
            return 'F-7'
    return ""

def check_espaces(text_cell):
    pattern_espace = "( +)"
    for space in re.findall(pattern_espace,text_cell):
        n_spaces = len(space)
        if n_spaces != 1 and n_spaces %4 != 0:
            print(f"{n_spaces} nombre d'espaces")
            return "I-2"
    return ""

def check_branchement_successifs(text_cell):
    pattern_espace = "( +)"
    for space in re.findall(pattern_espace,text_cell):
        n_spaces = len(space)
        if n_spaces > 12:
            print(f"{n_spaces} branchement successifs")
            return "C-1"
    return ""
