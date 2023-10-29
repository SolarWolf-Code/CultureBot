# CultureBot
A Discord bot to choose a country at random and provide simple stuff such as the name, capital, subregion, and population.

## Setup
My preferred setup is via Docker:
``` shell
docker pull ghcr.io/solarwolf-code/culturebot:latest
docker run -d \
    --name culturebot \
    -e GUILD_ID=YOUR_DISCORD_SERVER_ID \
    -e TOKEN=YOUR_DISCORD_BOT_TOKEN \
    ghcr.io/solarwolf-code/culturebot:latest
```

Or you can clone this repo locally via Python:
``` shell
git clone https://github.com/SolarWolf-Code/CultureBot.git  
pip install -r requirements.txt  
export GUILD_ID=YOUR_DISCORD_SERVER_ID # e.g. 123456789012345678  
export TOKEN=YOUR_DISCORD_BOT_TOKEN # e.g. abcdefghijklmnopqrstuvwxyz.1234567890.abcdefghijklmnopqrstuvwxyz
python3 culture_bot.py  
```


## How it works
When you get your bot up, it will have a csv file that it pulls the data from. This csv file was created using the [RESTContries
](https://restcountries.com/) REST API.


## Commands
`/rc` - Picks a random country and provides basic information about it.  
`/reset` - Resets the list of countries within the csv file.

## Personal Use
My personal use for this bot is to use it weekly to explore the different types of cuisine around the world.
I'd like to create a traditional dish from the country picked. Not only is this a fun way to improve my cooking skills but
also a way to learn about the culture of the country.
