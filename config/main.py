import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="m.", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="this server"))
    print("Bot sudah siap!")

@bot.event
async def on_member_join(member):

    channel = member.guild.system_channel
    
    await channel.send(f"Halo {member.mention}! selamat datang di {member.guild.name}")

@bot.command()
async def halo(ctx):
    await ctx.reply("Halo juga!")

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run(TOKEN)
