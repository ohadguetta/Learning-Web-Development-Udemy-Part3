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



# Write a function called unique_elements that takes in two lists as 
# input and returns a new list containing the unique elements from both lists, 
# in the order of their first occurrence.

def unique_list(lst1,lst2):
    lst3 = lst1[:] # or lst3 = list(lst1)
    for item in lst2:
        if item not in lst3:
            lst3.append(item)
    return lst3
print(unique_list([1,2,3,4],[2,3,4,7,8]))
print(unique_list(['a', 'b', 'c'], ['b', 'c', 'd']))


# Palindrome

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


# Write a function called capitalize_titles that takes a list of strings as input.
#  The function should capitalize the first letter of each word in the string if 
# the word is not one of the common English articles (i.e., "a", "an", "the"), 
# prepositions (i.e., "in", "on", "at"), or conjunctions (i.e., "and", "but", "or").
#  The function should return the modified list of strings.



def capitalize_words(*args):
    exceptions = ['a','or','and','of','the','an','at','in','on','at','but']
    for item in list(args):
        sentence = ''
        try:
            for word in item.split():
                if word not in exceptions:
                    sentence = sentence + str(word).capitalize() + ' '
                else:
                    sentence = sentence + str(word) + ' '
            return sentence
        except:
            return 'Error, maybe one of the values is not a string?'

print(capitalize_words('hello world','hello and welcome!', 'fireee and a rain!',123))



# Write a function called calculate_discount that takes in a string representing 
# an item name and its price, separated by a colon (e.g., "item_name:price"). 
# The function should calculate the discounted price based on the following rules:

# If the item name starts with "sale_" (case insensitive), apply a 20% discount.
# If the item name starts with "clearance_" (case insensitive), apply a 50% discount.
# If the item name does not start with either "sale_" or "clearance_", apply no discount.
# The function should return a string in the format "item_name:discounted_price".

def calculate_discount(value):
    if isinstance(value,str):
        name = value.split(':')[0]
        price = int(value.split(':')[1])
        if name.lower().startswith(('sale')):
            price = price * 0.8
        elif name.lower().startswith(('clearence')):
            price = price * 0.5
        return name+':'+str(round(price,2))

print(calculate_discount('item1:100'))
print(calculate_discount('Sale_item1:56'))
print(calculate_discount('Clearence_item1:230'))

