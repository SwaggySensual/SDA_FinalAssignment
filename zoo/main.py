from zoo import Zoo
from animal import Animal
from zone import Zone
from employee import Employee
from task import Task

from time import sleep



from visitor import *


# Create tasks List
tasks = []

# add one Task of type Feed to the Zone with ID 1
tasks.append(Task(1, "Feed", 8, 1))

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


if __name__ == "__main__":
    print ("Starting Application")
    myzoo = MakeZoo()
    myzoo.OpenZoo()

    for i in range(1000):
        CheckFeedingTask(myzoo)
        AssignTask(myzoo)
        myzoo.Step()
        sleep(1)
        
