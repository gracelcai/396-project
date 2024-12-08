import csv
import argparse
import pandas as pd
from transformers import AutoModelForSequenceClassification

from pytorch_pretrained_bert.modeling import BertForSequenceClassification
import nltk
import os

nltk.download('punkt')

# model = AutoModelForSequenceClassification.from_pretrained('./models/finbert', ignore_mismatched_sizes=True)

# Use a pipeline as a high-level helper
from transformers import pipeline
from news_scraper import *

def news_results(symbol):
    pipe = pipeline("text-classification", model="ProsusAI/finbert")
    articles = get_news(symbol)
    results = []
    for article in articles['articles']:
        text = article['title']
        # text = article['description']
        pred = pipe(text)[0]
        article['label'] = pred['label']
        article['score'] = pred['score']
        results.append(article)
    return results
results = news_results('nvidia')
print(results)
# df = pd.read_csv('./news/nvidia.csv')

# def predict(row):
#     text = row['Title'].join(row['Description'])
#     pred = pipe(text)
#     return pred[0]['label'], pred[0]['score']

# df[['label', 'score']] = df.apply(predict)

# df.to_csv('./news/nvidia_results.csv')
# return df.to_dict()