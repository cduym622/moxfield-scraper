import requests
import json
import random
from config import user_agent_list
import helpers
from pathlib import Path

username = "ComedIan"

ids = helpers.getUserDecks(username)

base = Path(username)
base.mkdir(exist_ok=True)

for x in ids:
    helpers.convertIdToDecklist(x, "" + x + ".json", base)