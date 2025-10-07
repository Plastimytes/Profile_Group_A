#Base on trust communication and mood

class RTracker:
    def __init__(self, partner):
        self.partner = partner
        self.__trust = 50
        self._mood ="Happy"
        self._vibe = 100

    def build_trust(self, amount):
        if amount <=0:
            raise ValueError("Nooo")
        self._trust += amount

    def break_trust(self, amount):
        if amount <= 0:
            raise ValueError("Sorry")
        self._trust -= amount 

    def talk(self, duration):
        if duration <= 0:
             raise ValueError("Don't waste my time")
        self._vibe += duration
        self._trust += 5 
        self._mood ="Good"

netflix= RTracker("Chill")
netflix.build_trust(20)  

netflix._trust