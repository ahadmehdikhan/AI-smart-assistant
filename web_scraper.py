import requests
from bs4 import BeautifulSoup

def scrape_web(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find('div', class_='BNeawe').text
    return result
