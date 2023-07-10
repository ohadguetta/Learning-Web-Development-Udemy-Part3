def crazy():
    def count(num1,num2):
        print(str(num1+num2))
    count(1,2)

crazy()


num1 = 5
while num1 != 0:
    num1 -=1
    if num1 == 3:
        print('hello 3')
        pass # does fucking nothing!
        print('blop')
    print(num1)


print('-----')


num1 = 5
while num1 != 0:
    num1 -=1
    if num1 == 3:
        print('hello 3')
        continue
    print(num1)
