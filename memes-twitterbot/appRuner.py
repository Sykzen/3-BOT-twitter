import discord
from _token import *
from discord.ext import commands

bot=commands.Bot(command_prefix=prefixeBot ,description= "Bot memes twitter")
@bot.event
async def on_ready(): #to show "TranslateBot Joue à T.help"
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Twitter Comedie club"))
    @bot.command(name='help')
    async def help(ctx, submodule = ""):

bot.run(Token)
print("Working")