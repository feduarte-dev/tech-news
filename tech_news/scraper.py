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
    data = Selector(text=html_content)

    return {
        "url": data.css('link[rel="canonical"]::attr(href)').get(),
        "title": data.css("h1.entry-title::text").get().strip(),
        "timestamp": data.css(".meta-date::text").get(),
        "writer": data.css(".author a::text").get(),
        "reading_time": int(
            data.css(".meta-reading-time::text").get().split()[0]
        ),
        "summary": "".join(data.xpath("(//p)[1]//text()").getall()).strip(),
        "category": data.css(".category-style .label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
