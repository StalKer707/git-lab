from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def express(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getAge(self):
        pass

    @abstractmethod
    def getAgeInHumanYears(self):
        pass
