"""
class Pencil():
    def __init__(self, lead, material,brand,style,color):
        self.lead = lead
        self.material = material
        self.brand = brand
        self.style = style
        self.color = color
    def write(self, style):
        cursive = 0
        regular = 0
        if self.style == 'cursive':
            choose.font('Yellowtail')
            print('cursive')
        else:
            print('regular')
    def draw(self, color):
        self.color = art
pencil = Pencil(0.2,'wood','USA','cursive','orange')
pencil.draw('blue')
pen = Pencil(0.7,'metal','China','regular','silver')

class bank_account():
    def __init__(self,name,account_number,total_balance):
        self.name = name
        self.account_number = account_number
        self.total_balance = total_balance
    def depositing(self,add):
        self.total_balance = self.total_balance + add
    def withdrawal(self,subtract):
        if self.total_balance-subtract<0:
            print('sorry, you do not have enough money in your account')
            print(self.total_balance)
        else:
            self.total_balance = self.total_balance - subtract
    def balance(self):
        print(self.total_balance)
b1 = bank_account('Jeremy',0,0)
print(b1.name)
print(b1.account_number)
print(b1.total_balance)
b1.depositing(100)
b1.balance()
b1.withdrawal(1000)
b1.balance()

#8-11/12

class shopping_list():
    def __init__(self):
        self.dictionary = {}
    def add(self,item,number):
        if item in self.dictionary:
            self.dictionary[item] += 1
        if item not in self.dictionary:
            self.dictionary[item] = number
            print(self.dictionary)
    def remove(self,item):
        if self.dictionary[item]==1:
            del self.dictionary[item]
            print(self.dictionary)
        elif self.dictionary[item]>1:
            self.dictionary[item] -= 1
            print(self.dictionary)
b1 = shopping_list()
b1.add('apple',3)
b1.add('chicken',3)
b1.add('apple',1)
b1.add('people',1)
b1.subtract('apple')
b1.subtract('people')

#12-13
class phone_book():
    def __init__(self):
        self.dictionary = {}
    def add(self,name,number):
        if name in self.dictionary:
            print('you already have this person')
        else:
           self.dictionary[name] = number
        print(self.dictionary)
    def remove(self,name):
        i = input('are you sure you want to remove someone?')
        if name not in self.dictionary:
            print('you cannot delete this person again.')
            if i =='yes' or i=='Yes':        
                del self.dictionary[name]
        else:
            print('wise choice..')
        print(self.dictionary)
    def search(self,name):
        if name in self.dictionary:
            inp = self.dictionary[name]
            print('The number that corresponds to this name is',inp)
        else:
            print('This name is not yet in the phone book.')
    def update(self,name,number):
        if name in self.dictionary:
            self.dictionary[name] = number
        else:
            print('This name is not yet in the phone book.')
        print(self.dictionary)
b1 = phone_book()
b1.add('Jeremy',1904)
b1.update('Jeremy',1209)
b1.search('Jeremy')
"""
#14-17
class supermarket():
    def __init__(self):
        self.price = {'apple':2,'chicken':12,'broccoli':3}
        self.quantity = {'apple':2,'chicken':2,'broccoli':2}
    def buy(self):
        print(self.price)
        inp = input('what would you like to buy?')
        if  inp not in self.price:
            print('We dont even have that')
        elif self.price[inp] == 0:
            print('Im sorry, we ran out. Come back later, or dont; because our store sucks.')
        elif self.price[inp]>0:
            print('that will be',self.price[inp],'dollars')
        
    def ret(self):
        dairy = ['milk','eggs','yogurt','ice cream']
        inp = input('what would you be returning?')
        if inp in dairy:
            print('I am sorry, you cannot return dairy products IN THIS STORE!!!!!!!!!')
        else:
            self.quantity[inp] += 1
            print(self.quantity)
        print('thank you for your time')
b1 = supermarket()
b1.buy()
b1.ret()
b1.ret()
