score = 89

if score >= 101:
    print("Please verfiy your grade agian")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"    
    
    
print(f"Geade: ${grade}")    

