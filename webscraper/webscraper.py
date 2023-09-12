from flask import Flask
app =Flask(__name__)
import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    words = ''
    for word in soup.find_all("p"):
        words += (word.text)
    return words
link = "https://www.vox.com/science/2023/6/23/23771154/malaria-transmission-florida-texas-mosquitoes-risk-prevention-anopheles"

print(scrape_news(link))

