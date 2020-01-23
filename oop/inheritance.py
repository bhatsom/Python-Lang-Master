# https://www.techbeamers.com/python-inheritance/


class Car:
    def __init__(self, make, model, variant):
        self._make = make
        self._model = model
        self._variant = variant

    def getMake(self):
        return self._make

    def getModel(self):
        return self._model

    def getVariant(self):
        return self._variant

    def setVariant(self, variant):
        self._variant = variant


class SportsCar(Car):
    def __init__(self, make, model, variant, color):
        super(SportsCar, self).__init__(make, model, variant)
        self._color = color

    def getColor(self):
        return self._color

    def vehicleInfo(self):
        return self.getMake() + " " + self.getModel() + " " + self.getVariant() + " in " + self._color


c1 = SportsCar("Dodge", "Charger", "RT", "Tri-Quote Red")
print("c1: ", c1.vehicleInfo())


# class to create sports car with size definition
class SportsCarWithSize(SportsCar):
    def __init__(self, make, model, variant, color, size):
        super(SportsCarWithSize, self).__init__(make, model, variant, color)
        self._size = size

# override vehicleInfo()
    def vehicleInfo(self):
        return self.getMake() + " " + self.getModel() + " " + self.getVariant() + "in" + self.getColor() + " and size" + self._size


c2 = SportsCarWithSize("Ford", "Mustang", "GT", "Dark Grey", "Coupe")
print("c2 vehicleInfo: ", c2.vehicleInfo())

# access base class function
print("c2 vehicleInfo without Size: ", SportsCar.vehicleInfo(c2))

