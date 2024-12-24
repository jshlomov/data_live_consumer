from app.db.mongo_db import collection


def insert_news(news):
    news_list = news["news"]
    return collection.insert_many(news_list)