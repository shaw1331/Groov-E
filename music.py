import youtube_dl
import pafy
import asyncio  
import discord
from discord.ext import commands

class User(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self.song_q = {}

    self.setup()
  
  def setup(self):
    for guild in self.bot.guilds:
      self.song_q[guild.id] = []

  async def search_song(self, amount , song , get_url = false):








  @commands.command()
  async def join(self,ctx):
    if ctx.author.voice is None:
      return await ctx.send("You are not connected to any voice channel currently")

    if ctx.author.voice is not None:
      await ctx.voice_client.disconnect()

    await ctx.author.voice.channel.connect()

  @commands.command()
  async def leave(self,ctx):
    if ctx.voice_client is not None:
      return await ctx.voice_client.disconnect()

    await ctx.send("I am not connected to any voice channel!")