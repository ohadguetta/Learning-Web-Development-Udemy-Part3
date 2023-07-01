class Cup:
    broken = False
    color = 'red'

    def __init__(self,color,broken):
        self.color = color
        self.broken = broken

    def break_cup(self):
        self.broken = True
        return 'Broken!'
    def set_fire_to_cup(self):
        raise NotImplementedError
    
class MiniCup(Cup):
    def set_fire_to_cup(self):
        return 'fire was set to minicup!!!'
    def __init__(self, color, broken):
        super().__init__(color, broken)


