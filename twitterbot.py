import tweepy

# setup the twitter API keys
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# setup the tweepy API client
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def like_tweet(tweet_id):
    # like a tweet using the tweet_id
    api.create_favorite(tweet_id)
    print("Liked tweet with id:", tweet_id)

def comment_on_tweet(tweet_id, comment_text):
    # comment on a tweet using the tweet_id and comment_text
    status = "Commenting on tweet with id: " + str(tweet_id) + " with text: " + comment_text
    api.update_status(status=status, in_reply_to_status_id=tweet_id)
    print("Commented on tweet with id:", tweet_id, "with text:", comment_text)

def retweet_tweet(tweet_id):
    # retweet a tweet using the tweet_id
    api.retweet(tweet_id)
    print("Retweeted tweet with id:", tweet_id)

# Example usage
# like_tweet(123456)
# comment_on_tweet(123456, "This tweet is great!")
# retweet_tweet(123456)
