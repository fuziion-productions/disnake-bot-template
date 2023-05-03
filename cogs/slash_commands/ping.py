import disnake
from disnake.ext import commands


class SlashPingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ping', description='Shows the bot\'s latency.')
    async def slash_ping(self, ctx: disnake.ApplicationCommandInteraction):
        latency = round(self.bot.latency * 1000)
        await ctx.response.send_message(f'Pong! Latency: {latency}ms')


def setup(bot):
    bot.add_cog(SlashPingCog(bot))
