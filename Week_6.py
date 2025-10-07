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
