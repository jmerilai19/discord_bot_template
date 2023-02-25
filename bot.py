import discord
import yaml

from discord.ext import commands

if __name__ == "__main__":
    with open("./env/variables.yaml", "r") as f:
        variables = yaml.safe_load(f)
        
    TOKEN = variables["token"]

    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if message.content in ['hello', "hi", "hey", "yo", "sup"]:
            await message.channel.send('Hello!')

        await bot.process_commands(message)

    @bot.command()
    async def ping(ctx):
        await ctx.send(f'{round(bot.latency * 1000)} ms')

    bot.run(TOKEN)
