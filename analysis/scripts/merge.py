# this file is to merge the jupyter notebooks into one.
# source: https://towardsdatascience.com/how-to-easily-merge-multiple-jupyter-notebooks-into-one-e464a22d2dc4


import json
import copy

# functions
def read_ipynb(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_ipynb(notebook, notebook_path):
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f)


karel_notebook = read_ipynb('../Karel/milestone2_EDA.ipynb')
kaitlyn_notebook = read_ipynb('path')
shaheer_notebook = read_ipynb('path')

final_notebook = copy.deepcopy(karel_notebook)
final_notebook['cells'] = karel_notebook['cells'] + kaitlyn_notebook['cells'] + shaheer_notebook['cells']

# Saving the resulting notebook
write_ipynb(final_notebook, '../submitted/test.ipynb')
