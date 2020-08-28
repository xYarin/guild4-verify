"""
This cog is currently not in used and is being developed.
If you don't see this in the last commit, it works :)
Don't activate it if you see this please, your responsibility, for questions contact in discord - xYarin#2280

"""

from discord.ext import commands, tasks
import discord
from discord.utils import get
from guild import Guild
from player import Player



class DailyCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #!self.check.start()
        # self.server = self.bot.get_guild(599561897850699834)
        # print(self.server)
        #self.channel = get(self.server.channels, name='bot-update', type=discord.ChannelType.text)
    def member_role_names(self):
        server_members = self.member_role_objects()
        names = []            
        for name in server_members:
            names.append(name.name)
        return names

    def member_role_objects(self):
        server_members = []
        for member in self.server.members:
            for role in member.roles: 
                if role.name == "Member":
                    server_members.append(member)
        return server_members



    def cog_unload(self):
        return
        #!self.check.cancel()
    
    #@tasks.loop(hours=24.0)
    @commands.command()
    async def check(self, ctx):
        self.server = self.bot.get_guild(599561897850699834)
        print(self.server)
        g = Guild("Guild4")
        g.members = g.getMembers()
        await ctx.message.add_reaction('✅')
        names = self.member_role_names()
        members = self.member_role_objects()
        members.pop(0)
        role = get(self.server.roles, name="Member")
        for member in members:
            print(f"Nick is {member.nick}")
            print(f"Name is {member.name}")
            if member.nick == None:
                print("Member nick is None")
                player = Player(member.name)
            else:
                print("Member nick is not None")
                player = Player(member.nick)
            if not g.inGuild(player.uuid):
                await discord.Member.remove_roles(member, role)
                
                
            


        
        
        

    # @check.before_loop
    # async def before_printer(self): # Waiting to on_ready event
    #     await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(DailyCheck(bot))