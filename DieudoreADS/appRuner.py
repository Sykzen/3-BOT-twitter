import discord
from _token import *
from discord.ext import commands
bot = commands.Bot(command_prefix=prefixeBot)
bot=commands.Bot(command_prefix=prefixeBot ,description= "description")

#---------chose one of those to set an activity to the bot------------------

# Setting `Playing ` status
await bot.change_presence(activity=discord.Game(name="a game"))
# Setting `Streaming ` status
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
# Setting `Listening ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
# Setting `Watching ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

#-----cmd help--------
    @bot.command(name='help')
    async def help(ctx, submodule = ""):





#-----------------------------------------Run the bot---------------------
bot.run(Token)