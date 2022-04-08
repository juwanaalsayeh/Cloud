import requests
from pprint import pprint
recipe_url_template ='https://api.edamam.com/search?q={}&app_id=8228a6c6&app_key=bd00528170e470eae3f228cb5bc7a1fc&from=0&to=20'
APP_ID='8228a6c6'
API_KEY='bd00528170e470eae3f228cb5bc7a1fc'
recipe_url = recipe_url_template.format(ID = APP_ID, KEY = API_KEY)
resp = requests.get(recipe_url)

if resp.ok:
        recipe = resp.json()
else:
        print(resp.reason)

pprint(recipe)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

<form class="btn btn-outline-secondary"
                    type="button"
                    id="Search"
                    action="/result"
                    method="POST">
                        <input type="text" id="Key Ingredient">
                        <input class="file_search" type="Search">
                    </form>
