import httpx
import asyncio

from decouple import config


AIR_QUALITY_API_KEY = config("AQICN_API_KEY")
BASE_URL = config("AQICN_BASE_URL")


def search_stations(keyword: str = "macedonia") -> list:
    """
    Get all stations by keyword
    """
    url = f"{BASE_URL}search/"
    query = {
        "token": AIR_QUALITY_API_KEY,
        "keyword": keyword
    }
    response = httpx.get(url=url, params=query)
    response_dict = response.json()
    stations = []
    if response.status_code == 200 and "data" in response_dict:
        if not isinstance(response_dict["data"], str):
            stations = [city["station"]["url"] for city in response_dict["data"]]
    return stations


def get_tasks(client: httpx.AsyncClient, urls: list) -> list:
    tasks = []
    query = {
        "token": AIR_QUALITY_API_KEY
    }
    for url in urls:
        tasks.append(client.get(url=f"{BASE_URL}feed/{url}/", params=query))
    return tasks


async def async_get_air_quality(urls: list) -> list:
    """
    Asynchronously send requests to get air quality info for the given urls
    """
    results = []
    async with httpx.AsyncClient() as client:
        tasks = get_tasks(client, urls)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(response.json())
    return results


def get_air_quality() -> list:
    """
    Get all stations and then get air quiality index
    for the stations.
    """
    urls = search_stations()
    results = asyncio.run(async_get_air_quality(urls))
    cities = []
    for response in results:
        city = {
            "name": response["data"]["city"]["name"],
            "aqi": response["data"]["aqi"]
        }
        cities.append(city)
    return cities
