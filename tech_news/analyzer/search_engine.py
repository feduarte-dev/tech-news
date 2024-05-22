from tech_news.database import db, search_news


# Requisito 7
def search_by_title(title):
    result = []

    for news in search_news({"title": {"$regex": title, "$options": "i"}}):
        result.append((news["title"], news["url"]))

    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
