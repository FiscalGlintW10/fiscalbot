import discord
from discord.ext import commands, tasks
import datetime
from random import choice
import numpy as np
from discord.ext import tasks, commands
from discord.utils import get
from itertools import cycle
import timedelta
import aiohttp
import discord
import datetime
import warnings
from discord.ext import commands
from datetime import timedelta
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from typing import Optional


servers = []


from urllib import parse, request
from discord.ext.commands import cooldown, BucketType
import re
import asyncio
import functools
import itertools
import math
import random
import os
from dotenv import load_dotenv
import sqlite3
import aiohttp,ez_rq,ez_rq.util
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class Member(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(bot.online)


async def main():
    a = ez_rq.get('https://www.google.com')
    print(await a.text())
    b = ez_rq.post('https://www.google.com',data={'a':'b'})
    print(await b.text())
    c = ez_rq.put('https://www.google.com',data={'a':'b'})
    print(await c.text())
    d = ez_rq.patch('https://www.google.com',data={'a':'b'})
    print(await d.text())
    e = ez_rq.delete('https://www.google.com')
    print(await e.text())
    f = await ez_rq.util.json2attr(a) # or you can send the dictionary
    f.a = 'b'
    print(await ez_rq.util.attr2json(f))


MY_GUILD = discord.Object(id=yourguildidhere)



intents = discord.Intents.default()
intents.message_content = True
prefix = '!'
intents = discord.Intents().all()
bot = commands.Bot(command_prefix = prefix, intents=intents)


@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel):
      return
    else:
      await bot.process_commands(message)



class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

@bot.command(name="hello", brief='Sends a simple hello message.')
async def hello_world(ctx: commands.Context):
    await ctx.reply("Hello there, hope you're enjoying yourself!", mention_author=True)



@bot.command(name="win10dl", brief='Windows 10 ISO download link.')
async def win10dl(ctx: commands.Context):
    await ctx.reply("Download Windows 10: https://www.microsoft.com/en-us/software-download/windows10", mention_author=True)



@bot.command(name="win11dl", brief='Windows 11 ISO download link.')
async def win11dl(ctx: commands.Context):
    await ctx.reply("Download Windows 11: https://www.microsoft.com/en-us/software-download/windows11", mention_author=True)
  

@bot.command(name="ping", brief='Bot Latency.')
async def ping(ctx: commands.Context):
    await ctx.reply(f"Pong! {round(bot.latency * 1000)}ms")



@bot.command(name="about", brief='Sends some information about me.')
async def about(ctx: commands.Context):
    await ctx.reply("I am Fiscal's Secretary, built by FiscalGlintW10 exclusively for his server. I have a few fun commands, type `!help` to see them. Have fun!")


@bot.command(name="goodnight", brief='Sends a farewell sleep message.')
async def goodnight(ctx: commands.Context):
    await ctx.reply("Goodnight, Sleep well there!")


@bot.command(name="msserver", brief='Microsoft Discord Link.')
async def msserver(ctx: commands.Context):
    await ctx.reply("Microsoft Community: https://discord.gg/microsoft", mention_author=True)


@bot.command(name="googleserver", brief='r/Google Discord Link.')
async def googleserver(ctx: commands.Context):
    await ctx.reply("r/Google: https://discord.gg/google", mention_author=True)


@bot.command(name="appleserver", brief='r/Apple Discord Link.')
async def appleserver(ctx: commands.Context):
    await ctx.reply("r/Apple: https://discord.gg/apple", mention_author=True)


@bot.command(pass_context=True, brief='Shows a meme')
async def meme(ctx):
    embed = discord.Embed(title="Here's a cool meme!", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)


@bot.command(name="serverlink", brief='Sends a permanent server link.')
async def serverlink(ctx: commands.Context):
    await ctx.reply("https://discord.gg/qsjAJ82Bb5 is a never expiring link to The Fiscal Community.")



@bot.command(name="userinfo", brief="Sends an embed showing information of mentioned user.")
async def userinfo(ctx, user: discord.Member): # b'\xfc'
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=user.color)
    embed.set_author(name=f"User {user.display_name}#{user.discriminator}", icon_url=user.avatar.url)
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name="Username", value=user.mention, inline=False)
    embed.add_field(name="User ID", value=user.id, inline=False)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Member Join Position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format), inline=False)
    embed.add_field(name='Bot Status',value=user.bot,inline=False)
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.reply(embed=embed)
    if isinstance(ctx.channel, discord.DMChannel):
      return




@bot.command()
async def briefuserinfo(ctx, user: discord.Member):
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=user.color)
    embed.set_author(name=f"User {user.display_name}#{user.discriminator}", icon_url=user.avatar.url)
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name="Username", value=user.mention, inline=False)
    embed.add_field(name="User ID", value=user.id, inline=False)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format), inline=False)
    return await ctx.reply(embed=embed)
    if isinstance(ctx.channel, discord.DMChannel):
      return
  

  

class Mathematics(commands.Cog):
    def __init__(self, client):
        self.client = client


      
@bot.command(brief='Adds the two integers sent.')
async def add(ctx, numOne: int, numTwo: int):
    await ctx.reply(numOne + numTwo)


@bot.command(brief='Multiplies the two integers sent.')
async def multiply(ctx, numOne: int, numTwo: int):
    await ctx.reply(numOne * numTwo)


@bot.command(brief='Subtracts the two integers sent.') 
async def subtract(ctx, numOne: int, numTwo: int):
    await ctx.reply(numOne - numTwo)


@bot.command(brief='Divides the two integers sent.')
async def divide(ctx, numOne: int, numTwo: int):
 try:
  await ctx.reply(numOne / numTwo)
 except ZeroDivisionError:
  await ctx.reply("Division by 0 is undefined.")


@bot.command(brief='Percents the two integers sent.')
async def percent(ctx, numOne: int, numTwo: int):
    await ctx.reply(numOne / numTwo * 100 )


@bot.command(brief='Sends the square of sent integer.')
async def square(ctx, numOne: int):
    await ctx.reply(numOne * numOne)


@bot.command(brief='Sends the cube of sent Integer.')
async def cube(ctx, numOne: int):
    await ctx.reply(numOne * numOne * numOne)





class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client



      

@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send(ctx.channel.mention + " has been locked successfully!")
    embed = discord.Embed(title="Channel Locked", description=f"{ctx.author.mention} has locked {ctx.channel.mention}.", timestamp=datetime.datetime.utcnow(), color=discord.Color.red)
    channel = bot.get_channel(1067096975100624967)
    await channel.send(embed=embed)
  

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=None)
    await ctx.send(ctx.channel.mention + " has been unlocked successfully!")
    embed = discord.Embed(title="Channel Unlocked", description=f"{ctx.author.mention} has unlocked {ctx.channel.mention}.", timestamp=datetime.datetime.utcnow(), color=discord.Color.green)
    channel = bot.get_channel(1067096975100624967)
    await channel.send(embed=embed)
  
    
  


@bot.command(brief='Kicks a certain member.',aliases=['k']) 
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord. Member,*, reason= "No reason provided"):
  embed = discord.Embed(title="User Kicked!", description=f"{ctx.author.mention} `[{ctx.author.id}]` has kicked {member.mention} `[{member.id}]` from the server for reason: " +reason, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())

  channel = bot.get_channel(1067096975100624967)
  await channel.send(embed=embed)
  await member.send("You have been **kicked** from The Fiscal Community. Reason: " +reason)
  await member.kick (reason=reason)


@bot.command(brief='Deletes past messages in the current channel')
@commands.has_permissions(manage_messages = True)
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send("**{}** messages have been purged! This message will self-destruct in 10 seconds.".format(amount), delete_after=10.0)



@bot.command(brief='Send a member a message you want the bot to.')
@commands.has_permissions(manage_messages = True)
async def dm(ctx, member : discord.Member,*, arg):
 try:
  await member.send(arg)
  await ctx.send('DM sent!')
 except:
  await ctx.send('I do not have enough permissions to DM this user. They may have blocked me or left the server.')

time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}

def convert_time_to_seconds(time):
    try:
        return int(time[:-1]) * time_convert[time[-1]]
    except:
        return time

  
@bot.command(brief='Bans a certain member.',aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*,reason= "No reason provided"):

 try:
  embed = discord.Embed(title="Guild Ban Added!", description=f"{ctx.author.mention} `[{ctx.author.id}]` has banned {member.mention} `[{member.id}]` from the server for reason: " +reason, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())

  channel = bot.get_channel(1067096975100624967)
  await channel.send(embed=embed)
  await ctx.send(f"<:CheckMark:1067095758844731483> Banned {member.mention} [{member.id}]")
  await member.send("You have been banned from The Fiscal Community. Reason: "+reason)
  await member.ban(delete_message_days=0, reason=reason)
 except discord.ext.commands.errors.MemberNotFound:
  await ctx.send("The Member was not found!") 




@bot.command(brief='Bans a certain member and removes messages.',aliases=['sb'])
@commands.has_permissions(ban_members = True)
async def softban(ctx, user : discord.User,*,reason= "No reason provided"):

 try:
  embed = discord.Embed(title="Guild Ban Added!", description=f"{ctx.author.mention} `[{ctx.author.id}]` has banned {user.mention} `[{user.id}]` from the server for reason: " +reason, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())

  guild = ctx.guild
  channel = bot.get_channel(1067096975100624967)
  await channel.send(embed=embed)
  await ctx.send(f"<:CheckMark:1067095758844731483> Banned {user.mention} [{user.id}]")
  await user.send("You have been banned from The Fiscal Community. Reason: "+reason)
  await guild.ban(discord.Object(id=user.id), reason=reason)
 except discord.ext.commands.errors.MemberNotFound:
  await ctx.send("The Member was not found!")

   



@bot.command(brief='Bans a user not in the server')
@commands.has_permissions(ban_members = True)
async def forceban(ctx, user : discord.User,*,reason= "No reason provided"):
 try:
  embed = discord.Embed(title="Guild Ban Added!", description=f"{ctx.author.mention} `[{ctx.author.id}]` has banned {user.mention} `[{user.id}]` from the server for reason: " +reason, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())

  guild = ctx.guild
  channel = bot.get_channel(1067096975100624967)
  await channel.send(embed=embed)
  await ctx.send(f"<:CheckMark:1067095758844731483> Banned {user.mention} [{user.id}]")
  await guild.ban(discord.Object(id=user.id),delete_message_days=0, reason=reason)
 except discord.ext.commands.errors.MemberNotFound:
  await ctx.send("The Member was not found!")


@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user: discord.User):
 try:
  embed = discord.Embed(title="Guild Ban Removed!", description=f"{ctx.author.mention} `[{ctx.author.id}]` has unbanned {user.mention} `[{user.id}]` from the server", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
  
  user = discord.Object(id=user.id)
  await ctx.guild.unban(user)
  channel = bot.get_channel(1067096975100624967)
  await channel.send(embed=embed)
  await ctx.send(f"<:CheckMark:1067095758844731483> Unbanned {user.mention} [{user.id}]")
 except discord.ext.commands.errors.MemberNotFound:
   await ctx.send("The Member was not found!")






@bot.command(brief='Adds an infraction(warning) to a certain member.',aliases=['w'])
@commands.has_permissions(kick_members=True)
async def infadd(ctx, member : discord.Member,*,reason= "No reason provided") :
  
    embed = discord.Embed(title="Guild Infraction Added!", description=f"{ctx.author.mention} `[{ctx.author.id}]` has added an infraction for {member.mention} `[{member.id}]` for reason: " +reason, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())

    await ctx.send(f"<:CheckMark:1067095758844731483> Added infraction to {member.mention} [{member.id}]")
    channel = bot.get_channel(1067096975100624967)
    await channel.send(embed=embed)
    await member.send("Infraction added in The Fiscal Community: " +reason)
    await member.infadd (reason=reason)

  

@bot.command(brief='Removes an infraction(warning) from a certain member.')
@commands.has_permissions(kick_members=True)
async def infrem(ctx, member : discord.Member) :
    embed = discord.Embed(title="Guild Infraction Removed!", description=f"{ctx.author.mention} `[{ctx.author.id}]` has removed an infraction from {member.mention} `[{member.id}]`", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())

    await ctx.send(f"<:CheckMark:1067095758844731483> Removed infraction from {member.mention} [{member.id}]")
    channel = bot.get_channel(1067096975100624967)
    await channel.send(embed=embed)
    await member.send("Your infraction has been cleared in The Fiscal Community.")
    await member.infrem


from discord.ext.commands import has_permissions





@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def report(ctx, member : discord.Member,*,reason= "No reason provided"):
    channel = bot.get_channel(1067463859138461836)
    embed = discord.Embed(title="User Report Received", description=f"{ctx.author.mention} `[{ctx.author.id}]` has reported {member.mention} `[{member.id}]` for reason: " +reason, timestamp=datetime.datetime.utcnow(), color=discord.Color.blurple())
    await channel.send(embed=embed)
    await ctx.author.send("This is an automated message sent to notify you that your member report was received and the Supervision Council have been alerted of it. They will take necessary action upon the reported member.\n\nThank you for using the The Fiscal Community Report System.")
    await ctx.message.delete()





@bot.command(brief='Quarantines a certain member.',aliases=['qr'])
@commands.has_permissions(kick_members=True)
async def quarantine(ctx, member : discord.Member) :
    embed = discord.Embed(title="Alright, I've isolated them in the spookiest place ever!", description=f"Hey {ctx.author.mention} `[{ctx.author.id}]`, {member.mention} `[{member.id}]` has been **quarantined** in The Fiscal Community.", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())

    await ctx.send(embed=embed)
    quarantined_role = ctx.guild.get_role(967810628955820142)
    verified_role = ctx.guild.get_role(942646283397656607)

    await member.send("You have been **quarantined** in The Fiscal Community.")
    await member.add_roles(quarantined_role)
    await member.remove_roles(verified_role)
    await member.quarantine




@bot.command()
async def thread(ctx,*, name):
    Textchannel = bot.get_channel(1009108692169400452)
    guild = ctx.guild
    thread = guild.get_thread()
    await Textchannel.create_thread(name=name,message=ctx.message)
    await thread.send(f"Thank you for creating a support thread {ctx.author.mention}. Please ask your question here. We'll reach back to you as soon as we can.")
    await ctx.message.delete()



@bot.command()
async def feedback(ctx,*,arg):
    channel=bot.get_channel(1067463859138461836)
    await channel.send(f"{ctx.author.mention} sent feedback: " +arg)
    await ctx.author.send(f"Hey there {ctx.author.mention}! This is an automated message to inform you that we have received your feedback. The Supervision Council of the server will review your suggestions and reach back to you as soon as they can.\n\nThank you for using the Fiscal Community Feedback Portal!")
    await ctx.message.delete()

  


from discord.ext import commands

warnings.filterwarnings("ignore", category=DeprecationWarning)
bot.session = aiohttp.ClientSession()

async def timeout_user(*, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with bot.session.patch(url, json=json, headers=headers) as session:
        if session.status in range(200, 299):
           return True
        return False


@bot.command(aliases=['m', 'mute', 't'], brief="Times out/mutes a server member.")
@commands.has_permissions(kick_members=True)
async def timeout(ctx: commands.Context, member: discord.Member, until: int):
    handshake = await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
    embed = discord.Embed(title="Alright, I've silenced them! ", description=f"Hey {ctx.author.mention} `[{ctx.author.id}]`, {member.mention} `[{member.id}]` has been **timed out** in The Fiscal Community for " +until, timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    if handshake:
         return await ctx.send(embed=embed)
         await member.send("You have been timed out in The Fiscal Community for " +until)
    await ctx.send("Something went wrong")


@bot.command(pass_context=True , aliases=["cn", "changenick", "cnick"])
async def nick(ctx, member: discord.Member, newnick):
    await member.edit(nick=newnick)
    await ctx.send(f'Hey {member.mention}, {ctx.author.mention} has changed your nickname.')

      







@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="The Fiscal Community", url="https://discord.gg/veNDhvck6N")) 
    print('Bot is running!')  




bot.run("token")
