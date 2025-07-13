n,m = map(int, input().split())
l = list(map(int,input().split()))
sort = sorted(l, reverse = True)
print(sum(sort[:m]))
