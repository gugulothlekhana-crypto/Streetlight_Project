streetlights = [
    ("Main Road", "Working"),
    ("Park Area", "Faulty"),
    ("School Road", "Working"),
    ("Market Area", "Faulty")
]

working = 0
faulty = 0

for location, status in streetlights:
    if status == "Working":
        working += 1
    else:
        faulty += 1

print("Working Streetlights:", working)
print("Faulty Streetlights:", faulty)

print("\nFaulty Streetlight Locations:")
for location, status in streetlights:
    if status == "Faulty":
        print(location)