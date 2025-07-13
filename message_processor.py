import json

from models import Article
from utils import normalize_text, tfidf_transform, predict


class MessageProcessor:
    def __init__(self):
        pass

    def process_message(self, channel, method_frame, header_frame, body):
        json_body = json.loads(body)

        article_text = json_body.get("article")

        article_text = normalize_text(article_text)

        tfidf_transformed = tfidf_transform(article_text)

        prediction = predict(tfidf_transformed)
        tag_prediction = prediction[0]

        article_id = json_body.get("id")

        Article.update({Article.tag: tag_prediction}).where(Article.id == article_id).execute()
