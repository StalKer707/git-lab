from .animal import Animal


class Turtle(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def getAgeInHumanYears(self):
        if self.getAge() <= 0:
            return 0

        return 15 + (self.getAge() - 1) * 2

    def express(self):
        print(r"""
       _____     ____
      /      \  |  o |
     |        |/ ___\|
     |_________/
     |_|_| |_|_|
        """)
