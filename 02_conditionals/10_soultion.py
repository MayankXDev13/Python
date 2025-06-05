pet = "Cat"
age = 2


if pet == "Dog":
    if age < 2:
        food = "Puppy food"
    else: 
        food = "Senior Dog food"
        
if pet == "Cat":
    if age < 2:
        food = "Junior Cat food"
    else: 
        food = "Senior Cat food"


print(f"AI Recommendation of your Pet is {pet} Food is {food}.")