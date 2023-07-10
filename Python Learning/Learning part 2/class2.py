name1 = 'Ohad'
name2 = name1
name3 = 'Ohad'

if name1 is name2:
    print('name1 is name2')
if name2 is name3:
    print('name2 is name3')
if name3 is name1:
    print('name3 is name1')

if not name1 is 'Bob':
    print('This is not bob!')
if name1 not in 'Bob':
    print('This is not bob!')