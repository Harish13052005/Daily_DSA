# Right rotation with direct slicing
'''
arr = list(map(int, input("Enter the list of numbers:").split()))
k = int(input("Enter the rotation value:"))

print(arr[-k:] + arr[:-k])
'''

# Right rotation with swapping & slicing
'''
def rotate(nums, k):
    def reverse(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    n = len(nums)
    k = k % n

    # Reverse the entire array
    reverse(0, n - 1)

    # Reverse the first k elements
    reverse(0, k - 1)

    # Reverse the remaining elements
    reverse(k, n - 1)

nums = list(map(int, input("Enter the array: ").split()))
k = int(input("Enter k: "))

rotate(nums, k)

print("Rotated array:", nums)
'''

# Left rotation
'''
arr = list(map(int, input("Enter the list of numbers:").split()))
k = int(input("Enter the rotation value:"))

print(arr[k:] + arr[:k])
'''

# Left rotation with swapping & slicing
'''
def rotate(nums, k):
    def reverse(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    n = len(nums)
    k = k % n

    # Reverse the entire array
    reverse(0, n - 1)

    # Reverse the first k elements
    reverse(0, n-k-1)

    # Reverse the remaining elements
    reverse(n-k, n - 1)

nums = list(map(int, input("Enter the array: ").split()))
k = int(input("Enter k: "))

rotate(nums, k)

print("Rotated array:", nums)
'''

# Check if Two Strings are Anagrams
'''
s1 = input("Enter the string 1:")
s2 = input("Enter the string 2:")

print(sorted(s1) == sorted(s2))
'''

# Reverse Every Word of a sentence
'''
sentence = input("Enter the sentence:")

words = sentence.split()

result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))
'''

#First Non-Repeating Character
'''
from collections import Counter

s = input("Enter the string:")

count = Counter(s)

for ch in s:
    if count[ch] == 1:
        print(ch)
        break
'''

# Check Sorted
'''
arr = list(map(int, input("Enter the list of numbers:").split()))

flag = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        flag = False
        break

print(flag)
'''

# Merge Two Sorted Arrays
'''
a = list(map(int, input("enter sorted array1:").split()))
b = list(map(int, input("enter sorted array2:").split()))

i = j = 0
result = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print(result)
'''

# Leaders in an Array
'''
arr = list(map(int, input("Enter the Array:").split()))

leaders = []

max_right = arr[-1]
leaders.append(max_right)

for i in range(len(arr) - 2, -1, -1):
    if arr[i] > max_right:
        max_right = arr[i]
        leaders.append(arr[i])

print(*leaders[::-1])
'''
