from time import sleep
from bs4 import BeautifulSoup
import requests


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}

    try:
        sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        print(f"Content Type: {response.headers['content-type']}")

        if response.status_code != requests.codes.ok:
            return None
        return response.text

    except requests.Timeout:
        print("Timeout durante a requisição.")
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    soup.prettify()
    array = []
    for item in soup.find_all("a", {"class": "cs-overlay-link"}):
        array.append(item['href'])
    if len(array) > 0:
        return array
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
