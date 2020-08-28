"""
This bot was made originally by xYarin for Guild4 Discord server to synchronize from guild members to server members automatically.
** All commnented code are commands that currently aren't in use. **

If you want to use it for your guild, add the bot with https://discord.com/oauth2/authorize?client_id=748897861952864268&scope=bot&permissions=8,
get your own hypixel API key with /api new in mc.hypixel.net, change the code from Guild4 to your guild name when the code says g =,
and also change the role name to your role name, here its "Member".
Also make sure to change the ID of the server to your server ID in daily_check.py

"""

import requests as r
from tokens import *
from player import Player
from guild import Guild
import discord
from discord.ext import commands
from discord.utils import get




client = commands.Bot(command_prefix='--')
g = Guild("Guild4")
        

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Guild4 Members!"))
    print("Bot is ready.")

def getRoles(member):
    roles = member.roles
    names = []
    for role in roles:
        names.append(role.name)
    return names

@client.event
async def on_member_join(member):
    server = client.get_guild(749009212671000700)
    channel = get(server.channels, name='general', type=discord.ChannelType.text)
    logs_channel = get(server.channels, name='bot-update', type=discord.ChannelType.text)
    role = get(member.guild.roles, name="Member")
    try:
        player = Player(member.name)
    except TypeError:
            embed=discord.Embed(title="Welcome!", description=f"Hello <@{member.id}>, welcome to Guild4 Discord Server!", color=0xd77d28)
            embed.set_author(name="Guild4 Verification Bot", icon_url=member.avatar_url)
            embed.add_field(name="Please change you nickname", value="In order to get the member role, change your discord nickname to your minecraft IGN", inline=False)
            embed.set_footer(text="Guild4 Bot by xYarin#2280")
            #await channel.send(f"Welcome! <@{member.id}>")
            await channel.send(embed=embed)
            embed=discord.Embed(title="Bot Logs", description=f"<@{member.id}> has joined, his name is not his IGN so I couldn't verify him", color=0xd77d28)
            embed.set_author(name="Guild4 Verification Bot", icon_url=member.avatar_url)
            embed.set_footer(text="Guild4 Bot by xYarin#2280")
            await logs_channel.send(embed=embed)
    else:
        if g.inGuild(player.uuid):
            await discord.Member.add_roles(member, role)
            embed=discord.Embed(title="Welcome!", description=f"Hello <@{member.id}>, welcome to Guild4 Discord Server!", color=0xd77d28)
            embed.set_author(name="Guild4 Verification Bot", icon_url=member.avatar_url)
            embed.add_field(name="Automatically Detected IGN", value="I saw you have the same username here as your minecraft IGN so I gave you the member role! Have fun :)", inline=False)
            embed.set_footer(text="Guild4 Bot by xYarin#2280")
            #await channel.send(f"Welcome! <@{member.id}>")
            await channel.send(embed=embed)
            embed=discord.Embed(title="Bot Logs", description=f"<@{member.id}> has joined, his name matches an IGN so I verified him automatically!", color=0xd77d28)
            embed.set_author(name="Guild4 Verification Bot", icon_url=member.avatar_url)
            embed.set_footer(text="Guild4 Bot by xYarin#2280")
            await logs_channel.send(embed=embed)

        else:
            embed=discord.Embed(title="Welcome!", description=f"Hello <@{member.id}>, welcome to Guild4 Discord Server!", color=0xd77d28)
            embed.set_author(name="Guild4 Verification Bot", icon_url=member.avatar_url)
            embed.add_field(name="Please change you nickname", value="In order to get the member role, change your discord nickname to your minecraft IGN", inline=False)
            embed.set_footer(text="Guild4 Bot by xYarin#2280")
            #await channel.send(f"Welcome! <@{member.id}>")
            await channel.send(embed=embed)
            embed=discord.Embed(title="Bot Logs", description=f"<@{member.id}> has joined, his name is not his IGN so I couldn't verify him", color=0xd77d28)
            embed.set_author(name="Guild4 Verification Bot", icon_url=member.avatar_url)
            embed.set_footer(text="Guild4 Bot by xYarin#2280")
            await logs_channel.send(embed=embed)
            
            
            

@client.event
async def on_member_update(before, after):
    if before.nick != after.nick:
        after_roles = getRoles(after)
        role = get(after.guild.roles, name="Member")
        if after.nick != None and before.nick != None:
            print(f"Nickname changed from {before.nick} to {after.nick}")
            player = Player(after.nick)
            if g.inGuild(player.uuid):
                print("Added member role")
                await discord.Member.add_roles(after, role)
            # elif "Member" in after_roles:
            #     print("Removed member role")
            #     await discord.Member.remove_roles(after, role)
        elif before.nick == None and after.nick != None:
            print(f"User changed his nickname for the first time from {before.name} to {after.nick}")
            player = Player(after.nick)
            if g.inGuild(player.uuid):
                print("Added member role")
                await discord.Member.add_roles(after, role)
            # elif "Member" in after_roles:
            #     print("Removed member role")
            #     await discord.Member.remove_roles(after, role)
        else:
            print(f"Nickname reseted from {before.nick} to {after.name}")
            player = Player(after.name)
            if g.inGuild(player.uuid):
                print("Added member role")
                await discord.Member.add_roles(after, role)
            # elif "Member" in after_roles:
            #     print("Removed member role")
            #     await discord.Member.remove_roles(after, role)
            


    


# client.load_extension('cogs.daily_check') cog is not working, go read daily_check.py
client.run(BOT_TOKEN)

