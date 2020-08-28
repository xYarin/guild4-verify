"""
Guild class - implement guilds objects from hypixel free API.
Using it to check if a player is in the member list

"""

import requests as r
from tokens import API_KEY



class Guild:
    def __init__(self, name):
        self.name = name
        self.data = r.get(f"https://api.hypixel.net/guild?name=guild4&key={API_KEY}").json()
    
    def getMembers(self):
        self.members = []
        for member in self.data['guild']['members']:
            self.members.append(member['uuid'])
        return self.members
    
    def inGuild(self, uuid):
        if uuid in self.getMembers():
            #print("You are in the guild!")
            return True
        #print("You are not in the guild!")
        return False

