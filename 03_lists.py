# 03_lists.py
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(justice_league)

justice_league.remove("Green Lantern")
justice_league.insert(justice_league.index("Aquaman")+1, "Green Lantern")
print(justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league.sort()
print("Sorted List:", justice_league)
print("New Leader:", justice_league[0])