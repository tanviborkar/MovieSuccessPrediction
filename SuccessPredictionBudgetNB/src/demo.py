from tweepy import Cursor
from textblob import TextBlob
from twitter_client import get_twitter_client
client=get_twitter_client()
#public_tweets = client.search('dark')
threshold=0
pos_sent_tweet=0
neg_sent_tweet=0
count=0
query = "chips movie"
for tweet in Cursor(client.search, q=query, rpp=100, count=20, result_type="recent", include_entities=True, lang="en").items(500):
	count=count+1
	analysis=TextBlob(tweet.text)
	if analysis.sentiment.polarity>=threshold:
		pos_sent_tweet=pos_sent_tweet+1
	else:
		neg_sent_tweet=neg_sent_tweet+1
if pos_sent_tweet>neg_sent_tweet:
	print("Overall Positive")
else:
	print("Overall Negative")
print(count)
print(query)