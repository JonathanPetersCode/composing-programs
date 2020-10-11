class Player:
    MAX_POSITION = 10

    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    @classmethod
    def move(cls, steps):
        if self.position + cls.steps < cls.MAX_POSITION:
            position += cls.steps
        else:
            self.position = cls.MAX_POSITION

    # This method provides a rudimentary visualization in the console
    def draw(self):
        drawing = "-" * self.position + "|" + "-" * \
            (Player.MAX_POSITION - self.position)
        print(drawing)


p = Player()
p.draw()
p.move(4)
p.draw()
p.move(5)
p.draw()
p.move(3)
p.draw()
