import discord
from discord.ext import commands
import os
import asyncio
from keep_alive import keep_alive

client = discord.Client()
bot = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=' THELITƎ'))






@bot.command(pass_context = True)
async def join(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("Fooking boomer haven't joined a vc")
  
  print("plays")
  await ctx.message.channel("plays")





@bot.command()
async def hello(ctx):
  channel = ctx.channel
  await channel.send("Hello, " + str(ctx.author.mention) + "!!")



# @bot.command(pass_context=True)
# async def join(ctx): 
#   if ctx.author.voice is None:
#       return await ctx.send("You are not connected to any voice channel currently!")

#   if ctx.author.voice is not None:
#     await ctx.voice_client.disconnect()

#   await ctx.author.voice.channel.connect()


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