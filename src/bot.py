import sys
import json
import tweepy

from requests import get
from time import sleep

from os import getenv
from dotenv import load_dotenv


load_dotenv()

bearer_token = getenv("BEARER_TOKEN")
consumer_key = getenv("CONSUMER_KEY")
consumer_secret = getenv("CONSUMER_SECRET")
access_token = getenv("ACCESS_TOKEN")
access_token_secret = getenv("ACCESS_TOKEN_SECRET")

try:
    with open("archive.json", "r") as read:
        archive = json.load(read)
except FileNotFoundError or json.JSONDecodeError as e:
    archive = []
    print(f"{e}. archive.json will be created/replaced. A dictionary will be used instead.")


class Kanye(tweepy.Client):
    def __init__(self) -> None:
        super().__init__(
            bearer_token=bearer_token,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )

        auth = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret,
            access_token, access_token_secret
        )

        api = tweepy.API(auth)

        print("You have awoken Kanye.")

        self.main_loop()

    def post(self) -> None:
        quote = get("https://api.kanye.rest").json()["quote"]

        if quote not in archive:
            self.create_tweet(text=quote)
            self.archive_post(quote)

            print(f"The quote, \"{quote}\" has been posted and archived.")
        elif len(archive) == 122:
            self.create_tweet(text="Shit I'm out of ideas. Fuck, cya I guess.")
            sys.exit()

    @staticmethod
    def archive_post(quote: str) -> None:
        archive.append(quote)

        with open("archive.json", "w") as write:
            json.dump(archive, write)

    def main_loop(self) -> None:
        while True:
            self.post()
            sleep(3600*24)


client = Kanye()
