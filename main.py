from models.parrot import Parrot
from models.turtle import Turtle
from models.person import Person


def main():
    kesha = Parrot("Kesha", 2)
    zavala = Turtle("Zavala", 4)

    kesha.happybirthday()

    jack = Person("Jack", kesha)
    john = Person("John")

    jack.getPetInfo()
    john.getPetInfo()

    john.setPet(zavala)
    john.getPetInfo()


if __name__ == "__main__":
    main()
