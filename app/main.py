import re
import json

from datetime import datetime
from air_quality import get_air_quality, get_aqi_for_city
from twitter import post_tweet, search_twitter

text = """Предупредување ({}): Концентрацијата на ПМ 2.5 честички во {} изнесува {} μg/m3"""

air_quality = get_air_quality()
rex = re.compile(r"\(.+\)")
for city in air_quality:
    if city["aqi"] > 35:
        city_name = rex.findall(city["name"])[0]
        city_name = city_name.lstrip("(").rstrip(")")
        date = datetime.strftime(datetime.now(), "%d %b, %Y %H:%M")
        post_tweet(text.format(date, city_name, city["aqi"]))

query = "@zagaduvanje"
tweet_fields = "text,author_id,created_at"
response = search_twitter(query, tweet_fields)
if response.meta["result_count"] != 0:
    data = response.data
    try:
        with open("replied.json", "r") as file:
            replied = json.load(file)
    except FileNotFoundError:
        replied = []

    for tweet in data:
        tweet_id = tweet["id"]
        if tweet_id not in replied:
            replied.append(tweet_id)
            text = tweet["text"]
            city = text.replace("@zagaduvanje", "").strip()
            aqi = get_aqi_for_city(city)
            if aqi != -1:
                post_tweet(f"Концентрацијата на ПМ 2.5 честички во {city} изнесува {aqi} μg/m3", in_reply_to_tweet_id=tweet_id)
            else:
                post_tweet(f"Нема информација за концентрацијата на ПМ 2.5 честички во {city}", in_reply_to_tweet_id=tweet_id)

    with open("replied.json", "w") as file:
        json.dump(replied, file)



