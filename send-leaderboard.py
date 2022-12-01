#!/usr/bin/env python
import operator
import requests
import os
import json
from datetime import datetime

r = requests.get('https://adventofcode.com/2022/leaderboard/private/view/1899089.json', cookies={"session": os.environ['AOC_SESSION']})

leaderboard = json.loads(r.content)
members_dict = dict(leaderboard['members'])
members_list = [{"name": m["name"], "score": m["local_score"], "stars": m["stars"]} for m in members_dict.values()]
members_list.sort(key=operator.itemgetter('score'), reverse=True)

date = datetime.today().strftime("%d.%m.%Y")
header = f"**ottonova AOC 2022** [Leaderboard](https://adventofcode.com/2022/leaderboard/private/view/1899089) - {date}"
standings = "\n".join([f":star2:\t**{m['stars']: 3}** \t***{m['name']}***" for m in members_list])

mattermost_header = {"Content-Type": "application/json"}
mattermost_request = {
    "channel": "adventofcode",
    "username": "AOC 2022 - ottonova",
    "attachments": [{
        "color": "#99ff99",
        "text": header
    },{
        "color": "#ff00ee",
        "text": standings
    }]
}
mattermost_url = os.environ['MATTERMOST_WEBHOOK_URL']
send = requests.post(mattermost_url, headers=mattermost_header, data=json.dumps(mattermost_request))
with open("/home/p/projects/private/aoc2022/mm.log", 'a') as log:
    log.write(f"{date}, {send.status_code}\n")