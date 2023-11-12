import json

f = open("zh_en.json")
g = open("update.json")
old = json.loads(f.read())
new = json.loads(g.read())
f.close()
g.close()

for i in new:
    if i not in old:
        old[i]=new[i]

with open("zh_en.json", mode = "w", encoding="utf-8") as f:
    json.dump(old, f, ensure_ascii = False, indent = 4)