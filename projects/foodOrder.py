foods = {"kebab" : 100, "hamburger": 80, "pizza": 90}

orderedFoods = []
check = 0

while (True):
    selectedFood = input(f"Select a food from the list {foods} \n(type q to quit)")
    if selectedFood == "q":
        break
    
    if (selectedFood not in foods):
        print(f"We dont have this food, sorry. Available foods \n{foods}")
        continue

    orderedFoods.append(selectedFood)
    check += foods.get(selectedFood)

print(f"You ordered: {orderedFoods}")
print(f"Check: {check}")