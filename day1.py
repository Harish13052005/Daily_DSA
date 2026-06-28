# Reverse a String
'''
s = "Data Structures"
print(s)
print(s[::-1])
'''

# Reverse a number
'''
n = int(input("Enter the number:"))
print(n)
rev = 0
while n:
    rev = rev*10 + n%10
    n = n//10
print(rev)
'''

# Palindrome String
'''
s = input("Enter the String:")
if s[::-1] == s:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''

# Palindrome Number
'''
n = int(input("Enter the Number:"))
temp = n
rev = 0

while temp:
    rev = rev*10 + temp%10
    temp //= 10

if rev == n:
    print("Palindrome")
else:
    print("Not a Palindrome") 
'''

# Second largest Number
'''
l = list(map(int, input("Enter the numbers:").split(",")))
s = sorted(l)
print(s[-2])
'''

# Second longest String
'''
l = input("Enter the string elements:").split()
largest = ""
second_largest = ""

for i in l:
    if len(i) > len(largest):
        second_largest = largest
        largest = i
print(second_largest)
'''

# Nth longest string
'''
arr = (input("Enter the strings:").split())

arr.sort(key=len, reverse=True)

n = int(input("Enter n: "))

print(f"{n}th largest string:", arr[n-1])
'''

# Remove Duplicates
'''
arr = list(map(int, input("Enter list of numbers").split()))
result = []

for i in arr:
    if i not in result:
        result.append(i)

print(result)
'''

# Character Frequency
'''
s = input("Enter the string:")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0)+1
for k, v in freq.items():
    print(k, ":", v)
'''

# Missing Number
'''
arr = list(map(int, input("Enter the numbers:").split()))
n = len(arr)+1

expected = n*(n+1)//2
actual = sum(arr)

print(expected-actual)
'''

# Move Zeros to end
'''
arr = list(map(int, input("Enter the digits:").split()))
res = [i for i in arr if i != 0]
res += [0]*arr.count(0)
print(res)
'''

# Longest Word in a sentence
'''
sentence = input("Enter the sentence:").split()
longest = max(sentence, key=len)
print(longest)
'''

# Two Sum
'''
nums = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the target: "))

d = {}

for i, num in enumerate(nums):
    if target - num in d:
        print("Indices:", [d[target - num], i])
        break
    d[num] = i
else:
    print("No pair found")
'''

# Valid Parentheses
'''
s = input("Enter the parentheses string: ")

stack = []
pairs = {')': '(',']': '[','}': '{'}

for ch in s:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if not stack or stack.pop() != pairs[ch]:
            print(False)
            break
    else:
        print("Invalid input! Only (), {}, [] are allowed.")
        break
else:
    print(len(stack) == 0)
'''
