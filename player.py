"""
Player class - to implement player object from hypixel free API.
Using it to get player IGN, and UUID, then I can check if he is in the guild

"""

import requests as r
from tokens import API_KEY



class Player:
    def __init__(self, name):
        self.name = name.lower()
        self.data = r.get(f"https://api.hypixel.net/player?key={API_KEY}&name={self.name}").json()
        if self.data['player'] == None:
            raise TypeError("No name found")
        else:
            self.uuid = self.data['player']['uuid']



