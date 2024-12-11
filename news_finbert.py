import csv
import argparse
import pandas as pd
from transformers import AutoModelForSequenceClassification

from pytorch_pretrained_bert.modeling import BertForSequenceClassification
import nltk
import os

nltk.download('punkt')

# Use a pipeline as a high-level helper
from transformers import pipeline
from news_scraper import *
from datetime import date, timedelta, datetime

today = date.today()
def news_results(symbol):
    pipe = pipeline("text-classification", model="ProsusAI/finbert")
    
    day = today - timedelta(days=0)
    articles = get_news(symbol, 7, day)
    results = []
    total_score = 0
    
    for article in articles['articles']:
        date = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").date()
        if date < today:
            text = article['title']
            # text = article['description']
            pred = pipe(text)[0]
            label = pred['label']
            score = pred['score']
            article['label'] = label
            article['score'] = score
            results.append(article)
            print(f"article: {text}, label: {label}, score: {score}")
            if label == 'positive':
                total_score += score
            elif label == 'negative':
                total_score -= score
    return total_score

print('score:', news_results('nvidia'))