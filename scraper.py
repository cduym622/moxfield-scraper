import requests
import json
import random
from config import user_agent_list
import helpers

ids = helpers.getUserDecks("BWheelerMTG")

for x in ids:
    helpers.convertIdToDecklist(x, "" + x + ".json")