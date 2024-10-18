import requests
import random
import json
from config import user_agent_list

def getUserDecks(username):
        url = (
            "https://api.moxfield.com/v2/users/" +
            username + "/decks?pageNumber=1&pageSize=99999"
        )

        print(f"Grabbing <{username}>'s public decks from " + url)
        
        r = requests.get(url, headers={'User-Agent': user_agent_list[random.randint(0, len(user_agent_list)-1)]})
        j = json.loads(r.text)

        ids = [item["publicId"] for item in j["data"]]
        ids2 = open("id2.json", "w")
        json.dump(ids, ids2)
        deckIds = open("ids.json", "w")
        json.dump(j, deckIds)
        return j