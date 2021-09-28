import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import youtube_dl
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix = "-", description = "WhatUp")

class BotData:
  def __init__(self):
    self.welcome_channel = None
    self.goodbye_channel = None
  
botdata = BotData()


#bot events here
@bot.event
async def on_ready():
    print("Bot is ready!")
    # await ctx.guild.voice_client.disconnect()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=' THELITƎ'))

# ------------------------------------------------------------------------------------   

@bot.event
async def on_member_join(member):
  if botdata.welcome_chanel != None:
    await botdata.welcome_channel.send(f"Welcome to Elite! {member.mention}")
  else:
    print("Welcome channel was not set.")

@bot.event
async def on_member_leave(member):
  if botdata.goodbye_channel != None:
    await botdata.goodbye_channel.send(f"Your time has come! {member.mention}")
  else:
    print("Goodbye channel was not set.")

@bot.command()
async def set_welcome_channel(ctx,channel_name = None):
  if channel_name != None:
    for channel in ctx.guild.channels:
      if channel.name == channel_name:
        botdata.welcome_channel = channel
        await ctx.channel.send(f"Welcome channel has been set to: {channel.name}")
        await channel.send("This is the new welcome channel!")

  else:
    await ctx.channel.send("You didn't include the name of a welcome channel.")

@bot.command()
async def set_goodbye_channel(ctx,channel_name = None):
  if channel_name != None:
    for channel in ctx.guild.channels:
      if channel.name == channel_name:
        botdata.goodbye_channel = channel
        await ctx.channel.send(f"Goodbye channel has been set to: {channel.name}")
        await channel.send("This is the new goodbye channel!")

  else:
    await ctx.channel.send("You didn't include the name of a goodbye channel.")


@bot.command(pass_context=True)
async def dm(ctx, user : discord.User ,*,arg = None):
  if arg!=None and user!=None:
    try:
      # n = str - str[-5:]
      # uid = discord.utils.get(client.get_all_members(), name=n, discriminator=str[-4:]).id
      target = await bot.fetch_user(user)
      await target.send(arg)
      
      await ctx.channel.send("'" + arg + "'" + " has been sent to: " + user.name)
    
    except:
      await ctx.channel.send("Couldn't DM the given user.")
  else:
    await ctx.channel.send("User name and/or a message was not included")

# SIDDHARTH BEHNCHOD YEH HELP WALA FUNCTION PURA KARNA  

# @bot.command(pass_context = True)
# async def help(ctx):


# asdsd



















###############################################################################################################################
@bot.command(pass_context = True)
async def play(ctx, url = None):
  if(ctx.author.voice):
    # if(ctx.voice_client.channel!=ctx.author.voice.channel):
    #   await ctx.send("Already in a voice channel")
    # else:
      # source = discord.FFmpegPCMAudio('one.mp3')
      # ch = ctx.voice_client
    if(ctx.voice_client==None):
      channel = ctx.message.author.voice.channel
      await ctx.send("Joining " + str(ctx.author.voice.channel) + " channel")
      await channel.connect()
    if(ctx.voice_client):
      if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
        if(url):
          ctx.voice_client.stop()
          FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
          YDL_OPTIONS = {'format': "bestaudio"}
          vc = ctx.voice_client

          with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download = False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            # source = discord.FFmpegPCMAudio("one.mp3")
            vc.play(source)
            annc = ">>> Now playing {}".format(url)
            await ctx.send(annc)
            # block_text = 
            # embed=discord.Embed(title=player.current.title,url=f"https://youtube.com/watch?v={player.current.identifier}")
      else:
        await ctx.send("Currently playing in " + str(ctx.voice_client.channel))
        # await ch.play(source)
  else:
    await ctx.send("Join a fooking voice channel " + str(ctx.author.mention) + "!!")

  # await ctx.send(ctx.author.voice)
  # await ctx.send("ctx.author.voice")
  # await ctx.send(ctx.voice_client.channel)
  # await ctx.send("cdawwwwwwdd")
  # await ctx.send(ctx.author.voice.channel)
  # await ctx.send("ctxaadsce")
  # await ctx.send(ctx.message.author.voice.channel)
  # await ctx.send("plays")



@bot.command(pass_context = True)
async def quit(ctx):
  if(ctx.voice_client!=None):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("I left the voice channel")
  else:
    await ctx.send("I am not in a voice channel")

# @bot.command()
# async def play(ctx,url):
#   if(ctx.voice_client==None):
#     return
#   elif(url):
#     ctx.voice_client.stop()
#     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#     YDL_OPTIONS = {'format': "bestaudio"}
#     vc = ctx.voice_client

#     with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
#       info = ydl.extract_info(url, download = False)
#       url2 = info['formats'][0]['url']
#       # source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
#       source = discord.FFmpegPCMAudio("one.mp3")
#       vc.play(source)



###############################################################################################################################
@bot.command()
async def hello(ctx, message = None):
  channel = ctx.channel
  if(message):
    await channel.send("Hello, " + str(ctx.author.mention) + str(message) + "!!")
  else:
    await channel.send("Hello, " + str(ctx.author.mention) + "!!")





@commands.Cog.listener()
async def on_voice_state_update(self, member, before, after):
    
    if not member.id == self.bot.user.id:
        return

    elif before.channel is None:
        voice = after.channel.guild.voice_client
        time = 0
        while True:
            await asyncio.sleep(1)
            time = time + 1
            if voice.is_playing() and not voice.is_paused():
                time = 0
            if time == 10:
                await voice.disconnect()
            if not voice.is_connected():
                break
                

# @bot.command()
# async def add(ctx,url):
#   ctx.voice_client.stop()
#   FFMPEG_OPTIONS = {'before_options': '-reconnect 1- reconnect_streamed 1-reconnect_delay_max 5', 'options': '-vn'}
#   YDL_OPTIONS = {'format':"bestaudio"}
#   vc = ctx.voice_client

keep_alive()
bot.run(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))



# -------------Useful code snippets here----------


# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return
#   if message.content.startswith('-'):
#     if message.content.startswith('-hello'):
#       await message.channel.send("Hello {0.author.mention}!!".format(message))
#     elif message.content.startswith('-play'):
#       hehe()
#       join()
#     else:
#       await message.channel.send('*Confused unga bunga*')

# def hehe():
#   print('Hemlo')

# @bot.event
# async def on_message(message):
#     author: discord.User = message.author
#     if author == bot.user: 
#       return
#       # update_net_worth(str(author))
#     if message.content.startswith('-hello'):
#       await message.channel.send('Hello {0.author.mention}!!'.format(message))
#       # await message.channel.send('I GOT EXTRADITED! :(')
#     elif message.content.lower().startswith('!run'): 
#       await message.channel.send('unknow command')

# @bot.command(pass_context=True)
# async def join(ctx): 
#   if ctx.author.voice is None:
#       return await ctx.send("You are not connected to any voice channel currently!")

#   if ctx.author.voice is not None:
#     await ctx.voice_client.disconnect()

#   await ctx.author.voice.channel.connect()


# @client.event
# async def join(ctx):
#   channel = ctx.message.author.voice.voice_channel
#   await bot.join_voice_channel(channel)


# @bot.command()
# async def on_message(message):
#   if message.author == client.user:
#     return
#   await print(message)
#   if message.content.startswith('-hello'):
#     await message.channel.send('Hello {0.author.mention}!!'.format(message))
#   if message.content.startswith('-play'):
#     await message.channel.send('ERR - currently under work')


# @bot.command()
# async def vuvuzela(context):
#     # grab the user who sent the command
#     user=context.message.author
#     voice_channel=user.voice.voice_channel
#     channel=None
#     # only play music if user is in a voice channel
#     if voice_channel!= None:
#         # grab user's voice channel
#         channel=voice_channel.name
#         await client.say('User is in channel: '+ channel)
#         # create StreamPlayer
#         vc= await client.join_voice_channel(voice_channel)
#         player = vc.create_ffmpeg_player('vuvuzela.mp3', after=lambda: print('done'))
#         player.start()
#         while not player.is_done():
#             await asyncio.sleep(1)
#         # disconnect after the player has finished
#         player.stop()
#         await vc.disconnect()
#     else:
#         await client.say('User is not in a channel.')

# @client.command()
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()

# user=context.message.author