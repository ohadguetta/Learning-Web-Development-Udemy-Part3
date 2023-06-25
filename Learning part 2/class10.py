def print_num(*args):
    print(args)

#print_num(1, 3, 4, 7, 9)

def print_kwarg(name,*args,**kwarg):
    print(name)
    print(args)
    print(kwarg)

#print_kwarg('hello',1,2,3,4,something='hello',age=20)

def calculate_average(*args,**kwargs):

    total = 0
    for item in args:
        if type(item) == str:
            if not kwargs.get('ignore'):
                total = total + int(item)
        else:
            total = total + int(item)
    return total // len(args)

print(calculate_average(1,2,3,"30",4,5,6,ignore=False))

def reverse_dict(**kwargs):
    reverse = {}
    for key,value in kwargs.items():
        if key not in reverse.keys():
            reverse[str(value)] = key
    return reverse
print(reverse_dict(name='ohad',age=20,blop='ohad'))

def unique_list(lst1,lst2):
    lst3 = lst1[:] # or lst3 = list(lst1)
    for item in lst2:
        if item not in lst3:
            lst3.append(item)
    return lst3
print(unique_list([1,2,3,4],[2,3,4,7,8]))
print(unique_list(['a', 'b', 'c'], ['b', 'c', 'd']))

def is_palindrome(value):
    reverse = ''
    for item in str(value).lower():
        reverse =  item + reverse
    if reverse == value.lower():
        return True
    return False
def is_palindrome_quicker(value):
    return value == value[::-1]

print(is_palindrome('radar'))
print(is_palindrome('alll'))
print(is_palindrome('GrerG'))

print(is_palindrome_quicker('radar'))
print(is_palindrome_quicker('alll'))
print(is_palindrome_quicker('GrerG'))


