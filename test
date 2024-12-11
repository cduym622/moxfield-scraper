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
        # https://archidekt.com/search/decks?orderBy=-createdAt&owner=FastHandsTam&ownerexact=true
    url = (
        "https://archidekt.com/api/decks/cards/?orderBy=-createdAt&owner=" +
        username + "&ownerexact=true&pageSize=48"
    )
        #print("Getting user decks at = " + url) #Logging

    print(f"Grabbing <{username}>'s public decks from " + url)

    r = requests.get(url, headers={'User-Agent': user_agent_list[random.randint(0, len(user_agent_list)-1)]})
    j = json.loads(r.text)
        #f = open("archidektDecks.out", "w"); f.write(json.dumps(j)); f.close()
    userDecks = []
    for e in j["results"]:
            # {"Kalamax Control": "123567"}
        userDecks.append(e["id"])
        # printJson(userDecks)
    return userDecks

def getDecklist(deckId, filename, basePath):
        # https://archidekt.com/api/decks/ ID /small/
    url = f"https://archidekt.com/api/decks/{deckId}/"

        # print(f"Grabbing decklist <{deckId}> {url}")                        #Logging
    r = requests.get(url, headers={'User-Agent': user_agent_list[random.randint(0, len(user_agent_list)-1)]})
    jsonGet = json.loads(r.text)

    deckList = deepcopy(DeckListTemplate)
        # Skal konverteres fra tal til string

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