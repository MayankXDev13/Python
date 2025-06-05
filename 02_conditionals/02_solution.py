age = 18
day = "Wednesday"



# if age is >= 18 is ticket price is 12 and else ticket price value is 8
price = 12 if age >= 18 else 8



if day == "Wednesday":
    price = price - 2 
    # price -= 2
    

print(f"Ticket price for you is $ {price}")