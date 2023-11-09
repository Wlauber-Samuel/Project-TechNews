import requests
from fake_useragent import UserAgent
from time import sleep

RATE_LIMIT_DELAY = 1  # Delay de 1 segundo para respeitar o rate limit


def fetch(url):
    try:
        ua = UserAgent()
        headers = {"user-agent": ua.random}

        page = requests.get(url, headers=headers, timeout=3)
        page.raise_for_status()

        return page.text
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return None  # Retorna None para erros 404
        else:
            print(f"Erro na requisição: {e}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    finally:
        sleep(RATE_LIMIT_DELAY)


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


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
