import requests
import random
import json
from config import user_agent_list

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
    ids2 = open("id2.json", "w")
    json.dump(ids, ids2)
    # store the full json information from the original request
    deckIds = open("ids.json", "w")
    json.dump(j, deckIds)
    return j