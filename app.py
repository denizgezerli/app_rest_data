from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    BASE_URL = 'https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate"
    }
    query_params = {
        "limit": 10
    }
    response = requests.get(f"{BASE_URL}/CT12EH", headers=headers, params=query_params)

    if response.status_code == 200:
        data = response.json()
        restaurants = data.get('restaurants', [])
        return render_template('index.html', restaurants=restaurants)
    else:
        return "Failed to retrieve data from the API."

if __name__ == '__main__':
    app.run(debug=True)
