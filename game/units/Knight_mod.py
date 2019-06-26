from Warrior_mod import Warriors


class Knight(Warriors):

    def __init__(self, name):
        super().__init__(60)
        self.name = name

    def attack(self):
        print(self.name, 'has attacked with his sword!')
        self.exp += 0.3
