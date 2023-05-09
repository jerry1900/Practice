def say(self):
    print('I\'m saying')


NewPerson = type('NewPerson', (object,), dict(say=say, name='jerry'))

aNewOne = NewPerson()
aNewOne.say()

