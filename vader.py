from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


#df = pd.read_csv('filename')




sentences = ["Started with 15 AMZN $195 calls, trimmed 2 more today for $5K profit 💸. Down to 1 contract left, and we’re already over 300%! Can’t complain when it’s printing like a money press. Taking profits on the way up? That’s how you let the market work for you. 📈💨 #AMZN"]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    scores = vs['compound']
    print("{:-<65} {}".format(sentence, str(vs)))