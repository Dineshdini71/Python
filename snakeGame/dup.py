
#  Inhertiance Practice
class Animal:
    def __init__(self):
        self.num_eye = 2

    def breath(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Breath in Water")

    def swim(self):
        print("swim under water")


dini = Fish()
dini.breath()
dini.swim()
