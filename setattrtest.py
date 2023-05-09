def say():
    print('hello person')

class Person:
    pass


new_one = Person()
setattr(new_one, 'name', 'jerry')
setattr(new_one, 'talk', say)
print(getattr(new_one,'name'))
new_one.talk()
