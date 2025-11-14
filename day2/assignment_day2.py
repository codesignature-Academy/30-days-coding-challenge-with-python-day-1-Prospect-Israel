print("welcome to the time converter!")

minutes = int(input("enter total minutes:"))

hours = minutes // 60
remaining_minutes = minutes % 60

print(minutes, "minutes is equal to", hours, "hour(s) and", remaining_minutes, "minute(s).")



print("welcome to days converter")

minutes = 1440
day = minutes
days = int(input("enter number of days: "))
days_in_minutes = days * day

hours = days_in_minutes // 60
remaining_minutes = days_in_minutes % 60
print(days, "day(s) is equal to", hours, "hour(s) and", remaining_minutes , "minute(s)")