import re
import unicodedata

import joblib
import spacy

nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])

tfidf_transformer = joblib.load('./models/transformer.joblib')
model = joblib.load('./models/logistic_model.joblib')


def normalize_text(text: str):
    punctuation = r"[!\"#$%&'()*+,./:;<=>?@^_`{}~““”’\[\]\d]―❤′‘"
    space_chars = "[\n\r\t-]"

    text = re.sub(punctuation, "", text)
    text = re.sub(space_chars, " ", text)

    text = unicodedata.normalize("NFKD", text)
    text = text.strip().lower()

    tokens = nlp(text)
    lemma_text = ""

    for token in tokens:
        lemma = token.lemma_
        lemma_text += lemma

        lemma_text += " "

    return lemma_text


def tfidf_transform(text: str):
    x = tfidf_transformer.transform([text])

    return x


def predict(x):
    prediction = model.predict(x)
    return prediction
