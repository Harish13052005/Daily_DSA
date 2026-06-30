# Longest common prefix

'''
strs = ["flower","flow","flight"]

prefix = strs[0]

for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)                                                                                                                                
'''

# Majority Element (Boyer-Moore)
'''
nums = [2,2,1,1,2,2,2]

count = 0

for num in nums:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)
'''

# Product Except Self nums = [1,2,3,4]
'''
n = len(nums)


ans = [1]*n

left = 1
for i in range(n):
    ans[i] = left
    left *= nums[i]

right = 1
for i in range(n-1,-1,-1):
    ans[i] *= right
    right *= nums[i]

print(ans)f
'''

#    Longest Substring without repeating characters
'''
nums = [2,4,6,8,10]
nums = [2,4,6,8,10]
target = 8

l, r = 0, len(nums)-1

while l <= r:
    mid = (l+r)//2

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        l = mid+1
    else:
        r = mid-1
'''

#
