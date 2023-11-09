# Requisito 7
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 8
def search_by_date(date):
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d")
        new_format = (
            f"{date_format.day:02d}/"
            f"{date_format.month:02d}/"
            f"{date_format.year}"
        )
    except ValueError:
        raise ValueError("Data inválida")

    response = search_news({"timestamp": new_format})
    list_result = [(item["title"], item["url"]) for item in response]
    return list_result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
