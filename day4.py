# RAT Pattern

'''
def RAT(len, ch):
    for i in range(1,len+1):
        print(ch*i)

len = int(input("Enter the size:"))
ch = input("Enter a symbol:")
RAT(len, ch)
'''

# Binary search - only applicable on sorted arrays
'''
def Binary_search(nums, target):
    nums.sort()
    l,r = 0,len(nums)-1

    while l <= r:
        mid = (l+r)//2

        if nums[mid] == target:
            return mid
            break
        elif nums[mid] < target:
            l = mid+1
        else:
            r = mid-1

nums = list(map(int, input("Ener te list of numbers:").split()))
target = int(input("enter the target:"))
print(Binary_search(nums, target))
'''

# Duplicates Count

'''
def duplicates_count(arr):
    arr1 = sorted(arr)
    dup = 0

    for i in range(len(arr1)-1):
        if arr1[i] == arr1[i+1]:
            dup += 1
    return dup

arr = list(map(int, input("Enter the elements of array:").split()))
print(duplicates_count(arr))
'''

# Replace even numbers with max and odd numbers with min of array

def replace_minmax(arr):
    mini = min(arr)
    maxi = max(arr)

    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i] = maxi
        else:
            arr[i] = mini
    return arr

arr = list(map(int, input("Enter the numbers:").split()))
print(replace_minmax(arr))

# Sum of elements of a matrix

'''
def matrixsum(matrix):
    total = 0
    for row in matrix:
        for num in row:
            total += num
    return total

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter the matrix row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Matrix:")
print(matrix)

print("Sum of all elements:", matrixsum(matrix))
'''

# Longest Substring Without Repeating Characters

'''
s = input()

seen = {}
left = ans = 0

for right, ch in enumerate(s):
    if ch in seen and seen[ch] >= left:
        left = seen[ch] + 1
    seen[ch] = right
    ans = max(ans, right-left+1)

print(ans)
'''
