lst = [1,2,3,4,5]
dict = {
    'name':'hello',
    'age':20,
    }
print(dict.items())
for key,value in dict.items():
    print(key,value)

for value in dict.values():
    print(value)



for value in lst:
    if value==3:
        continue

    print(f'{value}')

name = "hello"
def proper():
    return name
print(proper())