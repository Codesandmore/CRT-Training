n = int(input())
day = list(map(int,input().split()))
night = list(map(int,input().split()))  
mins = int(input())
day = sorted(day)
night = sorted(night, reverse = True)
pay = 0
for i in range(0,n):
    total = day[i] + night[i]
    if total>mins:
        pay += (total - mins) * 100
print(pay)
