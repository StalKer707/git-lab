from .pet import Pet


class Person:

    def __init__(self, name: str, pet: Pet = None):
        self.__name = name
        self.__pet = pet

    def setPet(self, pet: Pet):
        self.__pet = pet

    def getPetInfo(self):
        print("--------------------")

        if self.__pet is None:
            print(f"{self.__name} has no pet yet")
            print("--------------------")
            return

        print(f"Pet for {self.__name} " "is named {self.__pet.getName()}")

        print(
            f"Age: {self.__pet.getAge()} year(s), "
            f"about {self.__pet.getAgeInHumanYears()} human years"
        )

        print("And it expresses itself like this:")

        self.__pet.express()

        print("--------------------")
