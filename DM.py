
@bot.command()
async def dm(ctx, user: discord.User,*,arg = None):
  if arg!=None and user!=None:
    try:
      target = await bot.fetch_user(user_id)
      await target.send(args)

      await ctx.channel.send("'" + arg + "'" + " has been sent to: " + target.name)
    
    except:
      await ctx.channel.send("Couldn't DM the given user.")
  else:
    await ctx.channel.send("User name and/or a message was not included")

@client.command()
async def dm(ctx, user: discord.User, *, message=None):
    if message == None:
        await ctx.send('You need to put a message')
    else:
        await user.send(message)
        await ctx.channel.purge(limit=1)
        await ctx.send('DM Sent')
        await ctx.author.send('"' + message + '"' + ' sent to ' + str(user))
        # just so i can see every dm (a bit creepy ik but hey it's my bot so i'll do it)
        print('"' + message + '"' + ' sent to ' + str(user))