user_input = 'Rock'
lst = ['Rock','Paper','Scissors']
if user_input in lst:
    print('Great!')

if 's' in 'Swore'.lower():
    print('s is in swore!')

st = {'Item1','Item2','Item3'}
if 'Item1' in st:
    print(True)


key = 'name'

dict = {
    'name': 'Ohad',
    'age': 20,
}
print(key in dict)
