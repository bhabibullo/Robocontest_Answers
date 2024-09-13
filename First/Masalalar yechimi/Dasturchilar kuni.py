def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                valid = True
            else:
                valid = False
        else:
            valid = True
    else:
        valid = False
    
    return valid

year = int(input())
correctness = is_leap_year(year)

if len(str(year)) != 4:
    result = 4 - len(str(year))
    for i in range(result):
        year = '0' + str(year)

if correctness == True:
    print(f"12/09/{year}")
else:
    print(f"13/09/{year}")
