import disnake
from disnake.ext import commands


class GlobalEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            activity=disnake.Activity(
                name=f"github.com/REFUZIION",
                type=disnake.ActivityType.watching
            ),
            status=disnake.Status.online
        )

    @commands.Cog.listener()
    async def on_connect(self):
        print(f"Logged in as {self.bot.user}!")


def setup(bot):
    bot.add_cog(GlobalEvents(bot))
