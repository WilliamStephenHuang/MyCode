from abc import abstractmethod


class Builder():
    name = ""

    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    @abstractmethod
    def Hello(self):
        pass


class Thin(Builder):
    def Hello(self):
        print(self.name, "is a thin")


class Fat(Builder):
    def Hello(self):
        print(self.name, "is a fat")


class Director():
    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.Hello()


if __name__ == '__main__':
    thin = Thin('William')
    fat = Fat('Huang')
    director_thin = Director(thin)
    director_thin.draw()
    director_fat = Director(fat)
    director_fat.draw()
