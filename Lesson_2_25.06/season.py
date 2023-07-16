def season(month):
    if month in ("December", "January", "February"):
        return "Winter"
    if month in ("March", "April", "May"):
        return "Spring"
    if month in ("June", "July", "August"):
        return "Summer"
    if month in ("September", "October", "November"):
        return "Autumn"
#print(season(str(input("Input a month:" '\n'))))