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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your inner voice"))
    print("Bot sudah siap!")

@bot.event
async def on_member_join(member):

    channel = member.guild.system_channel
    
    await channel.send(f"Halo {member.mention}! selamat datang di {member.guild.name}")

@bot.command()
async def halo(ctx):
    await ctx.reply("Halo juga!")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="tanpa alasan"
    await ctx.guild.kick(member)
    await ctx.send(f"{member.mention} telah di kick karena {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="tanpa alasan"
    await ctx.guild.ban(member)
    await ctx.send(f"{member.mention} telah di ban karena {reason}")

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run(TOKEN)
