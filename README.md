# Disnake Bot

This is a Disnake bot that includes both a regular chat command and a slash command cog.

## Installation

To install the Disnake bot, you should first clone the repository:

```commandline
git clone https://github.com/fuziion-productions/disnake-bot-template.git
```


Create a virtual environment and install the dependencies:

```commandline
cd disnake-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


Finally, you should edit the `.env` file with the following contents:
```commandline
BOT_PREFIX=!
BOT_TOKEN=your-bot-token-here
```

Replace `your-bot-token-here` with your bot token, which you can obtain from the Discord developer portal.

## Usage

To run the Disnake bot, activate the virtual environment:

```commandline
source venv/bin/activate
```


Then, run the `bot.py` script:

```commandline
python bot.py
```


The bot will log in and be ready to use. You can use the `!ping` command to check the bot's latency, or use the `/ping` slash command to do the same thing.

Enjoy!


