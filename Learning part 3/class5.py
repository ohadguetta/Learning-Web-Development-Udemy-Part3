def wrapper_func(func):
    def wrappered():  
        print('hello')
        func()
    return wrappered
 
@wrapper_func
def myfunc():
     print('Hello this is myfunc')
           
myfunc()