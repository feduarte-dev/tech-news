from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    result = []

    for news in search_news({"title": {"$regex": title, "$options": "i"}}):
        result.append((news["title"], news["url"]))

    return result


# Requisito 8
def search_by_date(date):
    result = []

    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )

        for news in search_news({"timestamp": {"$regex": formatted_date}}):
            result.append((news["title"], news["url"]))

        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    result = []

    for news in search_news(
        {"category": {"$regex": category, "$options": "i"}}
    ):
        result.append((news["title"], news["url"]))

    return result
