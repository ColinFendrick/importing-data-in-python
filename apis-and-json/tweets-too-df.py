import pandas as pd
import tweepy
import json

tweet_list = []

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        tweet_list.append(status)
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweet_list, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())
