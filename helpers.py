import requests
import random
import json
from config import user_agent_list , DeckListTemplate , CardFormatTemplate
from copy import deepcopy
from pathlib import Path

# gets all ids associated with a user
def getUserDecks(username):
    # set the url to include the specified username
    url = (
        "https://api.moxfield.com/v2/users/" +
        username + "/decks?pageNumber=1&pageSize=99999"
    )

    print(f"Grabbing <{username}>'s public decks from " + url)
    
    # send a request to get the information of a moxfield user
    r = requests.get(url, headers={'User-Agent': user_agent_list[random.randint(0, len(user_agent_list)-1)]})
    # load the response as a json
    j = json.loads(r.text)
    # extract all publicId's of decks associated with the user
    ids = [item["publicId"] for item in j["data"]]
    # store those id's in their own json
    return ids


def convertIdToDecklist(deckId, filename, basePath):

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


    decklistLocale = open(basePath / filename, "w")
    json.dump(deckList, decklistLocale)
