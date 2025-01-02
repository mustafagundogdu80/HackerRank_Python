def is_leap(year):
    leap = False
    # Write your logic here
    if (year % 4 == 0 and year % 400 not in [100 , 200, 300] ):
        leap = True
    return leap

year = int(input())
print(is_leap(year))
