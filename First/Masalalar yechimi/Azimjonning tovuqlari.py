def count_chickens(n):
    max_age = 12
    age_5 = 5
    age_7 = 7
    
    chicks = [0] * (n + 1)
    
    chicks[0] = 1
    
    for month in range(n+1):
        if month + age_5 <= n:
            chicks[month + age_5] += chicks[month]
        if month + age_7 <= n:
            chicks[month + age_7] += 2 * chicks[month]
        if month >= 12:
            chicks[month-12]=0
    
    return sum(chicks)

n = int(input())

total_chickens = count_chickens(n)

print(f"{total_chickens}")
