from .animal import Animal


class Parrot(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def getAgeInHumanYears(self):
        return self.getAge() * 5

    def express(self):
        print(f'{self.getName()}: "Hello!"')
        print(r"""
        \
        (o>
     \_//)
      \_/_)
       _|_
        """)
