import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Daftar command:
m.help             - Menunjukkan daftar command
m.p <keyword lagu> - Mencari lagu dan memutarnya
m.q                - Menunjukkan antrian lagu
m.skip             - Skip lagu yg sedang diputar ke lagu selanjutnya
m.clear            - Berhentiin lagu dan menghapus antrian lagu
m.leave            - Keluarin bot dari vc
m.pause            - Pause lagu yg sedang diputar
m.resume           - Lanjutin lagu yg sedang dipause
```
"""
        self.text_channel_list = []


    @commands.command(name="help", help="Menunjukkan daftar command")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)