# from animal import Animal
# from zone import Zone
# from employee import Employee
import os

class Zoo:
    def __init__(self, name, openHours, location):
        self.Name = name
        self.OpenHours = openHours
        self.Location = location
        self.Animals = []
        self.Zones=[]
        self.Employees = []

    def OpenZoo(self):
        print("Zoo is open")

    def CloseZoo(self):
        print("Zoo is closed")
    
    def AddAnimal(self, animal):
        self.Animals.append(animal)
    
    def AddZone(self, zone):
        self.Zones.append(zone)
    
    def AddEmployee(self, emp):
        self.Employees.append(emp)

    def GetZone(self, id):
        for zone in self.Zones:
            if zone.ID == id:
                return zone 
            
    def Step(self):
        _ = [zone.Step() for zone in self.Zones]
        
        self.print_zoo_info()


    def print_zoo_info(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
        print("Zoo Information:")
        zone_data = []

        # Prepare zone data
        for zone in self.Zones:
            zone_dict = {
                "Zone": zone.Biome,
                "Food": zone.FoodContainers,
                "Animals": [(animal.Breed, animal.Health) for animal in zone.Animals]
            }
            zone_data.append(zone_dict)

        # Print zones as rows and animals as columns
        print("{:<20} {:<20} {:<30}".format("Zone", "Food", "Animals"))
        print("-" * 70)

        for zone_info in zone_data:
            zone_name = zone_info["Zone"]
            food = zone_info["Food"]
            animals = ", ".join([f"{breed} ({health})" for breed, health in zone_info["Animals"]])

            print("{:<20} {:<20} {:<30}".format(zone_name, food, animals))

        