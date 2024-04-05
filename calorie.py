from temperature import Temperature


class Calorie:
    """
    Represent an optimal calorie intake for a person
    """

    def __init__(self, weight, height, age, temperature):
        self.w = weight
        self.h = height
        self.a = age
        self.t = temperature

    def calculate(self):
        result = 10 * self.w + 6.5 * self.h + 5 - self.t * 10
        return result


if __name__ == "__main__":
    temp = Temperature(country="italy", city="rome").get()
    calorie = Calorie(70, 175, 28, temp)
    print(calorie.calculate())
