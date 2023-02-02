import re

from air_quality import get_air_quality
from twitter import post_tweet


air_quality = get_air_quality()
rex = re.compile(r"\(.+\)")
for city in air_quality:
    if city["aqi"] > 110:
        city_name = rex.findall(city["name"])[0]
        city_name = city_name.lstrip("(").rstrip(")")
        text = f"Предупредување: Загадувањето измерено во {city_name} изнесува {city['aqi']}"
        post_tweet(text)
