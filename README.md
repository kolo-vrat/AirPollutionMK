# AirPollutionMK

The idea of this project is to get information about the air quality in Macedonia from [https://aqicn.org/] and then post a Tweet if the air quality is poor.

## Installation
***
**1. Dependencies** 
To install the needed dependencies you first need to have pipenv installed.

```shell
pip install pipenv
```

After that simply type

```shell
pipenv install
```

which will create a new virtual environment and install the needed dependencies.

To spawn a shell and activate the environment type
```shell
pipenv shell
```
**2. Environment variables**
All environment variables should be placed in the root drectory in .env file. The contents of the file should be as present:
```
AQICN_BASE_URL=...
AQICN_API_KEY=...
TWITTER_BASE_URL=...
TWITTER_API_KEY=...
TWITTER_API_SECRET=...
TWITTER_ACCESS_TOKEN=...
TWITTER_ACCESS_TOKEN_SECRET=...
TWITTER_BEARER_TOKEN=...
```

**3. Run the script**
Finally run the main.py script:
Windows:
```shell
python app/main.py
```
Linux:
```shell
python3 app/main.py
```