import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    try:
        data = Selector(text=html_content)
        return data.css(".cs-overlay-link::attr(href)").extract()
    except ValueError:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        data = Selector(text=html_content)
        return data.css(".next::attr(href)").get()
    except ValueError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
