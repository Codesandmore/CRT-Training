arr = [1,7,5,9,2,12,3]
k = 2
count = 0
if k == 0:
    nums = dict()
    for num in arr:
        nums[num] = nums.get(num,0) + 1
        count = len([m for m in nums if nums[m]>1])
else:
    un = list(set(arr))
    uni = sorted(un, reverse=True)
    for i in range (len(uni)):
        if abs(uni[i] - k) in uni[i+1:]:
            count += 1
print(count)
