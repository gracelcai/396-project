from newsapi import NewsApiClient
import os
import csv
import argparse
from dotenv import load_dotenv

load_dotenv()
parser=argparse.ArgumentParser()
parser.add_argument("symbol")
parser.add_argument("--filename")
args=parser.parse_args()

symbol = args.symbol
if args.filename:
   filename = args.filename
else:
    filename = symbol + ".csv"

# Create csv file
csvfile = open(os.path.join('news',filename), 'w', newline='')
writer = csv.writer(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['Title', 'Description', 'Content', 'Source', 'URL', 'PublishedAt'])

# Get the value of an environment variable
api_key = os.environ.get("NEWS_API_KEY")
print(f"api key: {api_key}")
newsapi = NewsApiClient(api_key=api_key)  # Get an API key from https://newsapi.org/

# List of desired sources
sources = [
    "the-motley-fool",
    "the-wall-street-journal", 
    "bloomberg",
    "business-insider"
]

# Get articles from these sources
articles = newsapi.get_everything(q=symbol,
                                  sources=",".join(sources), 
                                  language="en", 
                                  from_param='2024-12-01',
                                  page_size=100)

# Print article details
for article in articles['articles']:
    writer.writerow([article['title'], article['description'], article.get('content', 'No content available'), article['source']['name'], article['url'], article['publishedAt']])
    print(f"Title: {article['title']}")
    print(f"Source: {article['source']['name']}")
    print(f"URL: {article['url']}\n")
