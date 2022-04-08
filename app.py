from typing import Dict

import requests
import sqlite3 as sql
# import json
import urllib
from random import randint
from flask import Flask, render_template, url_for, request

from recireq import search_my_recipes, make_request, get_url_q, display_recipe_labels, select_from_index, \
    select_recipe_from_index, filter_response, display_recipe_dict, save_recipe, query_recipes

app= Flask(__name__)

FILENAME = "Recipes.html"
con = sql.connect(FILENAME)
C = con.cursor()

# ID set is used to ensure all recipes have unique ID
IDS = {-1}
APP_ID = '8228a6c6'
API_KEY = 'bd00528170e470eae3f228cb5bc7a1fc'
URL = f'https://api.edamam.com/search?/app_id=8228a6c6&app_key=bd00528170e470eae3f228cb5bc7a1fc'
app = Flask(__name__)


@app.route('/')
@app.route('/Recipes')
def Recipes():
    return render_template("Recipes.html")


def main():
    """
    This program allows the user to search for recipes online using the
    Edamam API. It also allows the user to save lookup info for favorite
    recipes into a database. Finally, the user can look up saved recipes.
    """
    print()
    command = ''
    while command.lower() != 'q':
        print("1) Find New Recipe")
        print("2) Search Saved Recipes")
        command = input("\t>> ")
        print()
        if command == '1':
            query_recipes()
        elif command == '2':
            search_my_recipes()
    C.close()

if __name__ == "__main__":
    app.run(debug=True)
