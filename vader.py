from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

f = open('scraper_config.json')
config = json.load(f)

def vader_analyze():
    
    df = pd.read_csv('tweets.csv')
    lookback = config['lookback_window']
    cutoff_date = datetime.now() - timedelta(days=lookback)
    df = df[df[df['time'] >= cutoff_date]['time'].dt.date != datetime.now().date()]

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