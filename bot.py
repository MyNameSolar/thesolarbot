#SolarBot by Solar#6119  <---Thats my Discord :)

import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
import asyncio

startup_extensions = ["Music"]
Bot = commands.Bot(command_prefix=";")

@Bot.event
async def on_ready():
    print ("Solar bot is ready")
    print ("I am running on" + Bot.user.name)
    print ("With the ID: " + Bot.user.id)

    class Main_Commands():
        def __init__(self, Bot):
            self.Bot = Bot

@Bot.command(pass_context=True)
async def ping(ctx):
    await Bot.say(":ping_pong: Ping!")

@Bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await Bot.say("The Username is: {}".format(user.name))
    await Bot.say("The Users ID is: {}".format(user.id))
    await Bot.say("The Users status is: {}".format(user.status))
    await Bot.say("The Users highest role is: {}".format(user.top_role))
    await Bot.say("The User joined at: {}".format(user.joined_at))

@Bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await Bot.say(":boot: Goodbye, {}. You're fokehn gay!".format(user.name))
    await Bot.kick(user)  

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            Bot.load_extension(extension) 
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))    

Bot.run("NDg3OTkwMTEyMTk0Mzk2MTYy.DnWHMg.poAEAgCCc_bKuW_RJC7jINRQRvI")