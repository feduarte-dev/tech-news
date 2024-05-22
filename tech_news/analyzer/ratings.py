from tech_news.database import get_collection


# Requisito 10
def top_5_categories():
    collection = get_collection()
    categories = collection.distinct("category")
    result = {}
    for category in categories:
        result[category] = collection.count_documents({"category": category})
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return [category[0] for category in sorted_result[:5]]
