from typing import Dict, List
import json as json
import random as rand
from googletrans import Translator



def get_quotes() -> List:
    with open("quotes.json") as quotes_file:
        quotes = json.load(quotes_file)

    return quotes

def get_random_quote() -> Dict:
    quotes = get_quotes()
    quote = rand.choice(quotes)
    return quote


def build_tweet(quote:Dict[str,str]) -> str:
    author = quote["Author"].strip(",")
    tweet = f"{quote['Quote']} \n {author}"

    return tweet

def check_validity(tweet: str) -> bool:
    return len(tweet) < 230

def get_tweet():
    while True:
        quote = get_random_quote()
        tweet = build_tweet(quote)
        if check_validity(tweet):
            return tweet




