n = int(input())
k = int(input())
l = list(map(int, input().split()))
left,right = 0,k
maxval = []
current_max = 0
while right != n+1:
    window = l[left:right]
    current_max = max(current_max,max(window))
    maxval.append(current_max)
    left += 1
    right += 1
print(maxval)
