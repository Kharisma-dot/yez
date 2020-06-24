import discord
from discord.ext import commands
import asyncio

TOKEN = "NzI1NDAwNjY4ODY0NTEyMTMw.XvOPaQ.pmgh1g5BEdmbJ_-ewnjZoJkWcFk"
client = commands.Bot(command_prefix=commands.when_mentioned_or(""), case_insensitive=True)
client.remove_command('help')
client = commands.Bot(command_prefix = '!r')

def check_team(ctx):
    return client.get_guild(723173750044098590).get_role(723174942400577547) in ctx.author.roles
@client.event
async def on_connect():
    await client.change_presence(activity=discord.Streaming(name="DM ME 4 HELP", url='https://www.twitch.tv/rbkisnice'))
    print('ModMail BLUE')

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if message.author != message.author.bot:
        if not message.guild:
            await client.get_guild(697092473406881813).get_channel(725400963732603020).send(f"User meniton {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n\n__**Message Content:**__\n{message.content}")

@client.command()
@commands.check(check_team)
async def pn(ctx, member: discord.Member, *, text):
    await member.send(text)

@client.event
async def on_resumed():
    print('reconnected')

client.run((TOKEN), reconnect=True)
