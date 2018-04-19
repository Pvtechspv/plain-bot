import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='?', owner_id=277981712989028353)
# To edit the bot prefix, change the command_prefix to the desired prefix.
# Change the owner_id to the ID of the owner. Defaults to ME.



@bot.event
async def on_ready():
    print('Bot is online!')
    
# Add your commands here.
    
    
if os.environ.get('TOKEN') is None:
    print('No token was found in Heroku config vars. To host the bot from another platform, please wait to input the token.')
    x = input('Input the TOKEN of the bot.')
    bot.run(str(x))
else:
    bot.run(os.environ.get('TOKEN'))
