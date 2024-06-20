from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    quote = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
        quote = random_quote()
    return render_template('index.html', weather=weather, news=news, quote=quote)



def get_weather(city):
    api_key = 'a1db76d80a9c6347b531e64c7713f406'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

@app.route('/news')
def get_news():
    api_key = '0778a83d9485492197b3d62ce436c0fe'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    return response.json().get('articles', [])

@app.route('/quotes')
def random_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    if response.status_code == 200:
        quote = response.json()
        return render_template('quotes.html', content=quote['content'], author=quote['author'])
    else:
        return render_template('quotes.html', content='Error retrieving quote', author='')

if __name__ == '__main__':
    app.run(debug=True)
