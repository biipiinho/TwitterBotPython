import os as os
import time as time
import tweepy as tweepy
import services as services


TWITTER_API_KEY ="sdf"
TWITTER_API_KEY_SECRET ="sdfsd"
TWITTER_ACCESS_TOKEN  ="sadasd-"
TWITTER_ACCESS_TOKEN_SECRET ="asdasd"

def get_twitter_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY,TWITTER_API_KEY_SECRET )
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    twitter_api = tweepy.API(
        auth, wait_on_rate_limit=True

    )
    return twitter_api


def write_tweet():
    tweet = services.get_tweet()
    twitter_api = get_twitter_api()
    twitter_api.update_status(tweet)

def run():
    while True:
        write_tweet()
        time.sleep(5)


if __name__ == "__main__":
    run()