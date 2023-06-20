lst = [1, 4, 5, 6, 7, 8]
print(lst[1::]) # [4,5,6,7,8] # Correct!
print(lst[2:3]) # [5,6] #Wrong!!! this is [5]
print(lst[-3::]) # [6,7,8] # Correct!
print(lst[-2:-3]) # [6,7] # Wrong! this is []
print(lst[-1:1]) # [5,6,7,8] #Wrong!! this is []

print(lst[-3:-2]) # [6]
print(lst[1:-1]) # [4, 5, 6, 7, 8] # Wrong!! this is [4, 5, 6, 7]

print('-----------------')

lst = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Example 1: Get the elements from index 3 to the end of the list
print(lst[3::])

# Example 2: Get every third element starting from index 2
print(lst[2::3])

# Example 3: Get the elements from index 5 to index 2 (backwards)
print(lst[5:1:-1]) # goes from 5 to 1(not included) and doing -1 steps

# Example 4: Get the last two elements
print(lst[-2::]) # 

# Example 5: Get every second element in reverse order
print((lst[::-1])[::2])

# Example 6: Get the middle three elements
middle  = len(lst) //2
print(lst[middle-1:middle+2])
