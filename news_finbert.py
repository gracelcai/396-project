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

def news_results(symbol):
    pipe = pipeline("text-classification", model="ProsusAI/finbert")
    articles = get_news(symbol)
    results = []
    score = 0
    for article in articles['articles']:
        text = article['title']
        # text = article['description']
        pred = pipe(text)[0]
        label = pred['label']
        score = pred['score']
        article['label'] = label
        article['score'] = score
        results.append(article)
        if label == 'positive':
            score += score
        elif label == 'negative':
            score -= score
    return score
