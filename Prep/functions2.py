def studentinfo (*args, **kwargs):
    print(args)
    print(kwargs)
    
courses = ['Math', 'Science']
info = {'name':'Parthip', 'age': '19'}
    
studentinfo(*courses, **info)