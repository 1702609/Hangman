import json

with open('stat.json', 'r+') as f:
    playlist = json.load(f)
    previousNumber = playlist["totalWin"]
    playlist["totalWin"] = previousNumber + 1
    f.seek(0)
    f.truncate()
    json.dump(playlist, f)