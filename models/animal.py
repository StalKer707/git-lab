from abc import abstractmethod
from .pet import Pet


class Animal(Pet):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def happybirthday(self):
        self._age += 1

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    @abstractmethod
    def express(self):
        pass

    @abstractmethod
    def getAgeInHumanYears(self):
        pass
