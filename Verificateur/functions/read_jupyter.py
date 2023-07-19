import json

def read_ipynb(file_name):
    """return a dict item with the cells of the jupyter notebook

    Args:
        file_name (_type_): _description_
    """
    with open(f"sample/{file_name}.ipynb") as file:
        text = json.load(file)
    dico = dict(text)
    return dico

def make_liste_cell(dico_ipynb):
    liste_cellule_code = []
    for cell in dico_ipynb["cells"]:
        if cell["cell_type"] == "code":
            liste_cellule_code.append(" ".join(cell["source"]))
    return liste_cellule_code