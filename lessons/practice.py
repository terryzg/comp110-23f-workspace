temps: dict()
temp: dict[str, int] = {"Florida": 72, "Raleigh": 56}

ice_cream: dict[str, float] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

ice_cream["mint"] = 52.1

print(ice_cream)

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)
print("Is mint in ice_cream?")
print("mint" in ice_cream)

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")