import json
import requests    
from copy import deepcopy
from config import DeckListTemplate , CardFormatTemplate, user_agent_list
import random
from pathlib import Path

archidektUrl = "https://archidekt.com"
username = "LostPlaneswalker"
base=Path(username)
base.mkdir(exist_ok=True)

def getUserDecks(username):
    url = (
        "https://archidekt.com/api/decks/cards/?orderBy=-createdAt&owner=" +
        username + "&ownerexact=true&pageSize=48"
    )

    print(f"Grabbing <{username}>'s public decks from " + url)

    r = requests.get(url, headers={'User-Agent': 
                user_agent_list[random.randint(0, len(user_agent_list)-1)]})
    j = json.loads(r.text)

    userDecks = []
    for e in j["results"]:
            # {"Kalamax Control": "123567"}
        userDecks.append(e["id"])
        # printJson(userDecks)
    return userDecks

def getDecklist(deckId, filename, basePath):
        # https://archidekt.com/api/decks/ ID /small/
    url = f"https://archidekt.com/api/decks/{deckId}/"

    r = requests.get(url, headers=
        {'User-Agent': user_agent_list[random.randint(0, len(user_agent_list)-1)]})
    jsonGet = json.loads(r.text)

    deckList = deepcopy(DeckListTemplate)

    for card in jsonGet["cards"]:
        cardFormat = deepcopy(CardFormatTemplate)
        cardFormat["name"] = card["card"]["oracleCard"]["name"]
        cardFormat["quantity"] = card["quantity"]

        deckList["mainboard"].append(cardFormat)
    
    decklistLocale = open(basePath / filename, "w")
    json.dump(deckList, decklistLocale)


ids = getUserDecks(username)
for x in ids:
    getDecklist(x, "" + str(x) + ".json", base)