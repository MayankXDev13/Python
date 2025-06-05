number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{number} x {i} = {number * i}")