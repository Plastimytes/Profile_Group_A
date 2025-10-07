#Base on trust communication and mood
trust = 100
mood = "happy"

class RTracker:
    def __init__(self, partner):
        self.partner = partner
        self._trust = 50
        self._mood ="Happy"