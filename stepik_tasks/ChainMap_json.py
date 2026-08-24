import json
from collections import ChainMap
with open("zoo.json", "r", encoding = "utf-8") as f:
    zoo = json.load(f)
    chainmap = ChainMap(*zoo)
    print(sum(chainmap.values()))