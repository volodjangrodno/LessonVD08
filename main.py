from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    quotes = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
        quotes = random_quote()
    return render_template('index.html', weather=weather, news=news, quotes=quotes)



def get_weather(city):
    api_key = 'a1db76d80a9c6347b531e64c7713f406'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = '0778a83d9485492197b3d62ce436c0fe'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    return response.json().get('articles', [])

def random_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    return response.json().get('content', 'author')

if __name__ == '__main__':
    app.run(debug=True)
