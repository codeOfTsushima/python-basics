#def hello_func():
    #return ("Hello functions \n"*4 )
#print(hello_func().upper) #.upper converts the string to uppercase charecters
#pass # Passes/ skips the argument
#print(hello_func())

#def hello_func(greeting, name = 'You'):
   # return '{},{}'.format(greeting ,name)   
#print(hello_func('HI ', name = 'parthip')) #This is greeting variable and only works inside the local scope not globally

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Math', 'Art', name = 'Parhtip', age = '19')
