import os
from dotenv import load_dotenv
from app.kafka_settings.consumer import consume_message
from app.repository.mongo_repository import insert_news

load_dotenv(verbose=True)

if __name__ == '__main__':
    consume_message(
        os.environ['TOPIC_NEWS_NAME'],
        insert_news
    )