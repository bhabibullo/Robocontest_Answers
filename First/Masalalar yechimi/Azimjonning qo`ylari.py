n=int(input())

if n%4!=0:
    print(-1)
elif n%4==0:
    n=n//4
    print(n*2)
