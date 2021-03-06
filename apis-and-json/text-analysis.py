import re
import pandas as pd

tweet_list = [{
    'text': 'cruz', 'lang': 'english'
}, {
    'text': 'trump', 'lang': 'english'
}]

def word_in_text(word, tweet):
    word = word.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False


# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]
df = pd.DataFrame(tweet_list, columns=['text', 'lang'])

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])
