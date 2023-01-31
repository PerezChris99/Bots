import tweepy
import time

# Insert your own API keys here
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize API object
api = tweepy.API(auth)

# Define a function to like tweets based on search query
def like_tweets(search_query):
    for tweet in tweepy.Cursor(api.search, search_query).items(10):
        try:
            tweet.favorite()
            print("Liked tweet by:", tweet.user.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# Define a function to comment on tweets based on search query
def comment_on_tweets(search_query, comment_text):
    for tweet in tweepy.Cursor(api.search, search_query).items(10):
        try:
            tweet.retweet()
            tweet.favorite()
            print("Commented on tweet by:", tweet.user.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# Define a function to follow accounts based on search query
def follow_accounts(search_query):
    for tweet in tweepy.Cursor(api.search, search_query).items(10):
        try:
            if tweet.user.followers_count > 1000:
                tweet.user.follow()
                print("Followed", tweet.user.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# Define a function to unfollow accounts with less than 1000 followers
def unfollow_accounts_less_than_1000():
    for friend in tweepy.Cursor(api.friends).items():
        try:
            if friend.followers_count < 1000:
                friend.unfollow()
                print("Unfollowed", friend.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# Define a function to unfollow accounts that don't follow back in less than 3 days
def unfollow_non_followers():
    for friend in tweepy.Cursor(api.friends).items():
        try:
            if (time.time() - friend.status.created_at.timestamp()) > (3 * 24 * 3600):
                friend.unfollow()
                print("Unfollowed", friend.screen_name)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# Call
