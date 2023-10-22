from zoo import Zoo
from animal import Animal
from zone import Zone
from employee import Employee
from task import Task
from visitor import Visitor
from time import sleep
from random import randint
import pygame
import sys

#------------------------------------DEFINITIONS-----------------------
# Load the assets
savannah = pygame.image.load('assets/Savannah.png')
tundra = pygame.image.load('assets/Tundra.png')
forest = pygame.image.load('assets/Forest.png')

wolf_img = pygame.image.load('assets/wolf.png')
fox_img = pygame.image.load('assets/fox.png')
lion_img = pygame.image.load('assets/lion.png')
elephant_img = pygame.image.load('assets/elephant.png')
hyena_img = pygame.image.load('assets/hyena.png')
polarbear_img = pygame.image.load('assets/polarbear.png')
articfox_img = pygame.image.load('assets/articfox.png')
blackbear_img = pygame.image.load('assets/blackbear.png')
cheetah_img = pygame.image.load('assets/cheetah.png')
deer_img = pygame.image.load('assets/deer.png')
ostrich_img = pygame.image.load('assets/ostrich.png')

zookeeper_img = pygame.image.load('assets/zookeeper.png')

# Use pygame.transform.scale to scale down the images
savannah = pygame.transform.scale(savannah, (512, 512))
tundra = pygame.transform.scale(tundra, (512, 512))
forest = pygame.transform.scale(forest, (512, 512))

wolf_img = pygame.transform.scale(wolf_img, (130, 130))
fox_img = pygame.transform.scale(fox_img, (130, 130))
lion_img = pygame.transform.scale(lion_img, (130, 130))
elephant_img = pygame.transform.scale(elephant_img, (130, 130))
hyena_img = pygame.transform.scale(hyena_img, (130, 130))
polarbear_img = pygame.transform.scale(polarbear_img, (130, 130))
articfox_img = pygame.transform.scale(articfox_img, (130, 130))
blackbear_img = pygame.transform.scale(blackbear_img, (130, 130))
cheetah_img = pygame.transform.scale(cheetah_img, (130, 130))
deer_img = pygame.transform.scale(deer_img, (130, 130))
ostrich_img = pygame.transform.scale(ostrich_img, (130, 130))

zookeeper_img = pygame.transform.scale(zookeeper_img, (75, 130))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#THIS NEEDS TO BE REMOVED AS IS A PLACEHOLDER
animal_health = {
    "Wolf": 100,
    "Fox": 100,
    "Lion": 100,
    "Elephant": 50,
    "Hyena": 100,
    "Polar bear": 20,
    "Artic fox": 100,
    "Black bear": 20,
    "Cheetah": 100,
    "Deer": 10,
    "Ostrich": 100
}

# Animals and their corresponding images
# Animals for each zone
forest_animals = {
    "Wolf": wolf_img,
    "Black bear": blackbear_img,
    "Deer": deer_img
}

savannah_animals = {
    "Lion": lion_img,
    "Elephant": elephant_img,
    "Hyena": hyena_img,
    "Cheetah": cheetah_img,
    "Ostrich": ostrich_img
}

tundra_animals = {
    "Fox": fox_img, 
    "Polar bear": polarbear_img
}

# Define zone names
zone_names = ["Forest", "Savannah", "Tundra"]

#Set screen dimensions
screen_width, screen_height = 1920, 1080  # Full HD resolution

# Set object dimensions for buttons and zones
button_width, button_height = 120, 40
zone_width, zone_height = 512, 512
spacing = 96  # Space between zones
top_margin = (screen_height - zone_height) // 2

# Calculate positions for zone images
forest_x = (screen_width - 3 * zone_width - 2 * spacing) // 2
savannah_x = forest_x + zone_width + spacing
tundra_x = savannah_x + zone_width + spacing

# Calculate positions for rectangles below zones
rectangle_y = screen_height - 100
rectangle_width = zone_width
rectangle_height = button_height * 2  # Height for the title and buttons

#Establish healthbar sizes
healthbar_width = 100
healthbar_height = 10

# Create tasks List
tasks = []

# add one Task of type Feed to the Zone with ID 1
tasks.append(Task(1, "Feed", 8, 1))


#----------------------------------------------FUNCTIONS----------------------------
# create a function which instanciates a zoo
def MakeZoo():
    zoo = Zoo("Eindhoven Zoo", (9,5), "Eindhoven")
    # Add Zone 1 size X north Tundra empty animals list ..
    zoo.AddZone(Zone(1, 10, "north", "Tundra", [], "Tundra Animal"))
    # Add Zone 2 size X East  Forest empty animals list ..
    zoo.AddZone(Zone(2, 10, "east", "Forest", [], "Forest Animal"))
    # Add Zone 3 size X South Savana empty animals list ..
    zoo.AddZone(Zone(3, 10, "south", "Savana", [], "Savana Animal"))
    # add polar bear and arctic fox to tundra
    zoo.Zones[0].AddAnimal(Animal(1, "Tundra Animal", "Polar Bear", 2, 60))
    zoo.Zones[0].AddAnimal(Animal(2, "Tundra Animal", "Arctic Fox", 5, 10))
    # add  hyenas, cheetahs, lions, elephants, ostrich to savana
    zoo.Zones[2].AddAnimal(Animal(3, "Savana Animal", "Hyena", 3, 24))
    zoo.Zones[2].AddAnimal(Animal(4, "Savana Animal", "Lion", 3, 24))
    zoo.Zones[2].AddAnimal(Animal(5, "Savana Animal", "Elephant", 3, 24))
    zoo.Zones[2].AddAnimal(Animal(6, "Savana Animal", "Ostritch", 3, 24))
    # add wolf, black bear and deer to forest
    zoo.Zones[1].AddAnimal(Animal(7, "Forest Animal", "Wolf", 2, 30))
    zoo.Zones[1].AddAnimal(Animal(8, "Forest Animal", "Black Bear", 7, 110))
    zoo.Zones[1].AddAnimal(Animal(9, "Forest Animal", "Deer", 4, 26))
    # Add Employee ...
    zoo.AddEmployee(Employee(1, 12, 5))

    return zoo

# Create a function to check for feeding task creation
def CheckFeedingTask(zoo):
    for zone in zoo.Zones:
        if zone.FoodContainers < 50:
            tasks.append(Task(0,"Feed", 0, zone.ID))


# create a function for assigning tasks
def AssignTask(zoo):
    for task in tasks:
        if task.GetStatus() == False:
            zoo.Employees[0].AssignTask(task)
            zoo.Employees[0].ExecuteTask(zoo.GetZone(task.ZoneID))




#-------------------------------------MAIN PROGRAM---------------------------
if __name__ == "__main__":
    print ("Starting Application")
    myzoo = MakeZoo()
    myzoo.OpenZoo()

    for i in range(1000):
        CheckFeedingTask(myzoo)
        AssignTask(myzoo)
        myzoo.Step()
        sleep(1)