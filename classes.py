class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email

    def greeting(self):
        return f'my name {self.name}'

class Costumer(User):
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.balance = 0

    def setBalance(self, balance):
        self.balance=balance
        

daniel=User('daie', 'emial')

print(daniel)
print(daniel.name)

daniel.name='andres'

print(daniel.name)
print(daniel.greeting())