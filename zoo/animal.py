import pygame

class Animal:
    def __init__(self, ID, animal_type, animal_breed, age, weight):
        self.ID = ID
        self.Type = animal_type
        self.Breed = animal_breed
        self.Age = age
        self.Health = 100 #hp
        self.Weight = weight

    def draw(self, screen, x, y, width, height):
        # Draw the animal image
        animal_img = self.get_animal_image()  # Implement this method to return the appropriate image based on the animal's breed
        animal_img = pygame.transform.scale(animal_img, (width, height))
        screen.blit(animal_img, (x, y))

        # Draw the health bar
        health_bar_width = 50
        health_bar_height = 10
        health_bar_x = x + (width - health_bar_width) // 2
        health_bar_y = y - health_bar_height - 5
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, health_bar_width * (self.Health / 100), health_bar_height))
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x + health_bar_width * (self.Health / 100), health_bar_y, health_bar_width * (1 - self.Health / 100), health_bar_height))

    # ... (other methods and attributes)

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