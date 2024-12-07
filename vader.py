from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def vader_analyze():
    df = pd.read_csv('tweets.csv')

    analyzer = SentimentIntensityAnalyzer()
    sum = 0
    i = 0
    for sentence in df['text']:
        vs = analyzer.polarity_scores(sentence)
        scores = vs['compound'] * (df['retweets'][i] + 1)
        #print("{} {} {}".format(scores, vs['compound'], df['retweets'][i]))
        if (vs['compound'] > -.5 and vs['compound'] < .5):
            continue
        else:
            sum += scores
        i += 1

    return(sum/len(df))

print(vader_analyze())