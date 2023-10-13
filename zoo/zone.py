#from animal import Animal

class Zone:

    def __init__(self, id, size, location, biome, animals, animalType):
        self.ID = id
        self.Size = size
        self.Location = location
        self.Biome = biome
        self.AnimalType = animalType
        self.Animals = animals
        self.FoodContainers = 0
        self.FoodNutritionValue = 10

    def AddAnimal(self, animal):
        self.Animals.append(animal)

    def GetAnimalCount(self):
        return self.Animals.count()

    def FillFoodContainers(self):
        self.FoodContainers = 100

    def GetFood(self, amount):
        self.FoodContainers -= amount
        return self.FoodContainers

    def Step(self):
        _ = [animal.Step() for animal in self.Animals]

        for animal in self.Animals:
            if self.FoodContainers > 0:
                if animal.Feed(self.FoodNutritionValue):
                    self.GetFood(animal.GetPortionValue())

            else:
                print("Food Containers are empty")