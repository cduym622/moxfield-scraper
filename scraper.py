import requests
import json
import random
from copy import deepcopy
from config import user_agent_list
import helpers


# Implements code by thebear123's MTG-to-XMAGE repo
# https://github.com/thebear132/MTG-To-XMage/tree/main


# let's avoid getting blacklisted

deckId = "6brXVsMDXEi5e8ZnX3aCwA"

DeckListTemplate = {  # Remember to deepcopy() when copying this template
    "format": "",       # Format
    "companions": [],   # List of <CardFormatTemplate>
    "commanders": [],   # List of <CardFormatTemplate>
    "mainboard": [],    # List of <CardFormatTemplate>
    "sideboard": []     # List of <CardFormatTemplate>
}

CardFormatTemplate = {
    "quantity": 0,
    "name": "",         # Lightning Bolt
}

ids = helpers.getUserDecks("BWheelerMTG")

url = "https://api.moxfield.com/v2/decks/all/" + deckId
# print(f"Grabbing decklist <{deckId}>")                        #Logging
r = requests.get(url, headers={'User-Agent': user_agent_list[random.randint(0, len(user_agent_list)-1)]})
jsonGet = json.loads(r.text)

deckList = deepcopy(DeckListTemplate)
deckList["format"] = jsonGet["format"]

if jsonGet["commandersCount"] != 0:
    for cmdr in jsonGet["commanders"]:
                cardFormat = deepcopy(CardFormatTemplate)
                specificCard = jsonGet["commanders"][cmdr]

                cardFormat["name"] = cmdr
                cardFormat["quantity"] = specificCard["quantity"]
                deckList["commanders"].append(cardFormat)

    if jsonGet["companionsCount"] != 0:
        print(url)
        for comp in jsonGet["companions"]:
                cardFormat = deepcopy(CardFormatTemplate)
                specificCard = jsonGet["companions"][comp]
                
                cardFormat["name"] = comp
                cardFormat["quantity"] = specificCard["quantity"]
                deckList["companions"].append(cardFormat)

    for card in jsonGet["mainboard"]:
            cardFormat = deepcopy(CardFormatTemplate)
            specificCard = jsonGet["mainboard"][card]

            cardFormat["name"] = card
            cardFormat["quantity"] = specificCard["quantity"]
            deckList["mainboard"].append(cardFormat)

    for card in jsonGet["sideboard"]:
            cardFormat = deepcopy(CardFormatTemplate)
            specificCard = jsonGet["sideboard"][card]

            cardFormat["name"] = card
            cardFormat["quantity"] = specificCard["quantity"]
            deckList["sideboard"].append(cardFormat)

decklist = open("decklist.json", "w")
json.dump(deckList, decklist)