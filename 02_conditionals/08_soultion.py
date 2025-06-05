password = "mayank"
password_len = len(password)


if password_len < 6:
    strength = "Week"
elif password_len <= 10:
    strength = "Medium"
    
elif password_len > 10:
    strength = "Strong"
    

print(f"Password strength is: {strength}")    