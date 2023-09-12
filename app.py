from flask import Flask, render_template, request
app =Flask(__name__)
from finallyusingit import calculator
import requests
from bs4 import BeautifulSoup
import validators


#Scrapes article text
def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    words = ''
    for word in soup.find_all("p"):
        words += (word.text)
    return words


#Determines result of the user input
@app.route('/', methods = ["POST", "GET"])
def home():
    if request.method == 'POST':
        if request.form.get('link') == '' and request.form.get('text') != '':
            input = request.form.get('text')
            processed_text = calculator(input).calc()
        elif request.form.get('link') != '' and request.form.get('text') == '':
            if validators.url(request.form.get('link')):
                input = scrape_news(request.form.get('link'))
                processed_text = calculator(input).calc()
            else:
                processed_text = "url not valid"
        
        else:
            processed_text = "input something valid"
        

        return render_template("index.html", processed_text = processed_text)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)