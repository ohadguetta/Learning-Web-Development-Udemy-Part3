def add_numbers(lst):
    total = 0
    for item in lst:
        total = total + item
        yield total #yielddddd will return this as a list of every occurrence

for item in add_numbers([1,2,3,4,5,6,1000]):
    print(item)

