from flask import Flask, render_template, request
import requests
import yaml

app = Flask(__name__)

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

BASE_URL = config['BASE_URL']
headers = config['headers']
query_params = config['query_params']
default_postcode = config['default_postcode']

@app.route('/', methods=['GET'])
def index():
    postcode = request.args.get('postcode', default_postcode)
    if postcode:
        postcode = postcode.replace(" ", "")
    
    response = requests.get(f"{BASE_URL}/{postcode}", headers=headers, params=query_params)

    if response.status_code == 200:
        data = response.json()
        restaurants = data.get('restaurants', [])
        return render_template('index.html', restaurants=restaurants, postcode=postcode, default_postcode=default_postcode)
    else:
        return "Failed to retrieve data from the API."

if __name__ == '__main__':
    app.run(debug=True)
