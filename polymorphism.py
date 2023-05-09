class Animal():
    def eat(self, who):
        who.eat()


class Pig():
    def eat(self):
        print('pig is eating')


class Dog():
    def eat(self):
        print('dog is eating')


new_animal = Animal()
new_animal.eat(Pig())
new_animal.eat(Dog())
