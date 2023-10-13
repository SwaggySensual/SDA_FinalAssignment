class Animal:
    def __init__(self, ID, animal_type, animal_breed, age, weight):
        self.ID = ID
        self.Type = animal_type
        self.Breed = animal_breed
        self.Age = age
        self.Health = 100 #hp
        self.Weight = weight


    def GetHealth(self):
        return self.Health

    def Step(self):
        if self.Health > 0:
            self.Health = int(self.Health - (self.Weight / 10) )
    
    def IsAlive(self):
        # if self.health == 0:
        #     return False
        # else:
        #     return True
        return False if self.Health <= 0 else True
    
    def Feed(self, nutrition_value):
        if self.Health > 80:
            return False
        if nutrition_value > self.Weight / 10:
            self.Health += self.Weight / 10
        else:
            self.Health += nutrition_value

        self.Health += nutrition_value
        if self.Health > 100:
            self.Health = 100
        return True

    
    def GetPortionValue(self):
        return int(self.Weight/10)




    

        
