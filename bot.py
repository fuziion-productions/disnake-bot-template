import os

import disnake
from disnake.ext import commands
from pydotenv import Environment

env = Environment()

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=env['BOT_PREFIX'], intents=intents)

if __name__ == '__main__':
    for dirPath, dirNames, filenames in os.walk('./cogs/'):
        for file in filenames:
            if not file.endswith('.py'):
                continue

            relative_path = os.path.relpath(os.path.join(dirPath, file), './cogs')
            module_name = relative_path.replace(os.path.sep, '.')[:-3]

            bot.load_extension(f"cogs.{module_name}")
            print(f"cogs.{module_name} has been loaded!")

bot.run(env['BOT_TOKEN'])
