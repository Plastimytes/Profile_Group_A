###ENCAPSULATION RUN THROUGH
##Create your class
coins=100
add=coins+500
print(f"I had {add} coins")

##OOP
class piggy_bank:
    def __init__(self, coins):
     self.coins=coins
     print(f"i currently have {self.coins}")
    
    def add(self, coins_add):
        if coins_add>0:
         self.coins+=coins_add
         print(f"I now have {self.coins} coins")
        else:
            print(f"No money")
     
    def get_balance(self):
        return self.coins 

p1=piggy_bank(100)
p1.add(5300)   

class pigybank:
    def __init__(self, coins):
        self._coins = 0
        self.put_in(coins)

#Setters (To create what is going to be there)
    def put_in(self, amount):
        if amount <=0:
            raise ValueError("Add real money")
        self._coins += amount

    def take_out(self, amount):
        if amount <=0:
            raise ValueError("Be Real")
        if amount > self._coins:
            raise ValueError("Money will come")
        self._coins -= amount                    

#Getter to display setter results    
    def how_Much(self):
        return self._coins

REM =pigybank(1000)
REM.take_out(344)

print("\n REM's box has:", REM._coins,"coins")
