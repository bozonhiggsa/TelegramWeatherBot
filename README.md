### Bot Telegram for getting current weather data
##### Implementation that provide of getting current weather data using Telegram bot

PyOWM is a client Python wrapper library for OpenWeatherMap (OWM) web APIs. It allows quick and easy consumption of OWM data from Python applications via a simple object.

Technologies:
- Python 3;
- Docker.

####Prerequisites
You need to install packages to project's environment (requirements.txt):
- certifi==2019.11.28
- chardet==3.0.4
- geojson==2.5.0
- idna==2.9
- pyowm==2.10.0
- pyTelegramBotAPI==3.6.7
- requests==2.23.0
- six==1.14.0
- urllib3==1.25.8

or simple perform:
- cd to root project's directory;
- run command - pip3 install -r requirements.txt

####Running via Terminal or IDE:
- You need to go to @BotFather (inside Telegram), create new bot and get your own unique token;
- You need to go to https://openweathermap.org/ and get your own unique API token;
- Change config.py with these tokens;
- Run the project - python3 bot.py.

####Running via Docker:
- set up Docker;
- enter to terminal;
- cd to root project's directory;
- build of Docker image:
  docker build -t weather_bot .
- launch Docker container:
  docker run --name weather -d --rm weather_bot

#### License

This project is licensed under the terms of the MIT license.