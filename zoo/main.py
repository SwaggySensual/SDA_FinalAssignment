from zoo import Zoo
from animal import Animal
from zone import Zone
from employee import Employee
from task import Task
from visitor import Visitor
from time import sleep
import random
import pygame
import sys

#------------------------------------DEFINITIONS-----------------------
# Load the assets
savannah = pygame.image.load('assets/Savannah.png')
tundra = pygame.image.load('assets/Tundra.png')
forest = pygame.image.load('assets/Forest.png')

animal_images = {
    
    "Wolf" : pygame.image.load('assets/wolf.png'),
    "Fox" : pygame.image.load('assets/fox.png'),
    "Lion" : pygame.image.load('assets/lion.png'),
    "Elephant" : pygame.image.load('assets/elephant.png'),
    "Hyena" : pygame.image.load('assets/hyena.png'),
    "Polar bear" : pygame.image.load('assets/polarbear.png'),
    "Arctic fox" : pygame.image.load('assets/arcticfox.png'),
    "Black bear" : pygame.image.load('assets/blackbear.png'),
    "Cheetah" : pygame.image.load('assets/cheetah.png'),
    "Deer" : pygame.image.load('assets/deer.png'),
    "Ostrich" : pygame.image.load('assets/ostrich.png')

}

guy_img = pygame.image.load('assets/guy.png')
girl_img = pygame.image.load('assets/girl.png')
zookeeper_img = pygame.image.load('assets/zookeeper.png')

#Scale down the unit image and make a flipped copy of it
zookeeper_img_L = pygame.transform.scale(zookeeper_img, (75, 130))
zookeeper_img_R = pygame.transform.flip(zookeeper_img_L, True, False)

girl_img_L = pygame.transform.scale(girl_img, (78, 130))                        
girl_img_R = pygame.transform.flip(girl_img_L, True, False)

guy_img_L = pygame.transform.scale(guy_img, (75, 130))                        
guy_img_R = pygame.transform.flip(guy_img_L, True, False)

# Use pygame.transform.scale to scale down the images
savannah = pygame.transform.scale(savannah, (512, 512))
tundra = pygame.transform.scale(tundra, (512, 512))
forest = pygame.transform.scale(forest, (512, 512))

scaled_animal_images = {key: pygame.transform.scale(img, (130, 130)) for key, img in animal_images.items()}

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Animals and their corresponding images
# Animals for each zone
forest_animals = {
    "Wolf": scaled_animal_images["Wolf"],
    "Black bear": scaled_animal_images["Black bear"],
    "Deer": scaled_animal_images["Deer"]
}

savannah_animals = {
    "Lion": scaled_animal_images["Lion"],
    "Elephant": scaled_animal_images["Elephant"],
    "Hyena": scaled_animal_images["Hyena"],
    "Cheetah": scaled_animal_images["Cheetah"],
    "Ostrich": scaled_animal_images["Ostrich"]
}

tundra_animals = {
    "Arctic fox": scaled_animal_images["Arctic fox"],
    "Polar bear": scaled_animal_images["Polar bear"]
}

animals = {}

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

#Define habitat sizes
habitat_width, habitat_height = (512, 512)

#Establish healthbar sizes
healthbar_width = 100
healthbar_height = 10
foodIndicator_height = healthbar_height*3

# Define one Add animals button dimensions and positions
add_button_width, add_button_height = 200, 60
add_button_x = (screen_width - add_button_width) // 2
add_button_y = screen_height - 80

#Creating the button
add_button = pygame.Rect(add_button_x, add_button_y, add_button_width, add_button_height)

#employee movement speed
employee_speed = -50
visitor_speed = -5

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
    zoo.AddEmployee(Employee(1, 8, 5))

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

def wallBounce(x, speed, left_wall, right_wall):
    #Check for hitting a wall. If so, change that direction.
    if x <= left_wall or x >= right_wall:
        speed = speed * -1

    #To be implemented maybe?
    #if self.y <= 0 or self.y >= self.maxHeight:
    #    self.ySpeed = self.ySpeed * -1

    return speed



#-------------------------------------MAIN PROGRAM---------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print ("Starting Application")
    # Initialize pygame
    pygame.init()

    # Create a font for labels
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 90)

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Define zone buttons with their corresponding zone indices
    zone_buttons = [
        pygame.Rect(forest_x, rectangle_y, rectangle_width, rectangle_height),
        pygame.Rect(savannah_x, rectangle_y, rectangle_width, rectangle_height),
        pygame.Rect(tundra_x, rectangle_y, rectangle_width, rectangle_height)
        ]  
    
    myzoo = MakeZoo()
    myzoo.OpenZoo()

    # Main loop
    running = True
    current_zone = None
    selected_animals = set()  # Store selected animals for the current zone
    animals_added = False #To check if the animals are added or not (make use of the button)
    # Define a boolean flag for placing the employees
    employee_flag = False
    visitor_flag = False
    FoodLevels = [0] * len(myzoo.Zones)

    while running:
        CheckFeedingTask(myzoo)
        AssignTask(myzoo)

        #Add a condition to only make the zoo work when animals are added
        if animals_added == True:
            myzoo.Step()

        sleep(0.5)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #Ckeck first if button is clicked
                if add_button.collidepoint(mouse_pos):
                        #Clear the selected_animals set before adding animals from the current zone
                        selected_animals.clear()
                        # Add all animals to the selected_animals set for each zone
                        selected_animals.update(forest_animals.keys())
                        selected_animals.update(savannah_animals.keys())
                        selected_animals.update(tundra_animals.keys())
                        animals_added = True  # Set the flag to indicate animals are added

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Clear the screen
        screen.fill((192, 192, 192))

        # Draw zoo title
        title_text = "ZOO"
        title_font = pygame.font.Font(None, 90)
        title_text_surface = title_font.render(title_text, True, black)
        text_rect = title_text_surface.get_rect(center=(screen_width // 2, 50))
        screen.blit(title_text_surface, text_rect)

        for i, zone in enumerate(myzoo.Zones):
            FoodLevel = zone.FoodContainers
            FoodLevels[i] = FoodLevel
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Draw zones with black borders
        zones = [forest, savannah, tundra]
        # Draw zone images
        zone_x_positions = [forest_x, savannah_x, tundra_x]
        for i, zone_image in enumerate(zones):
            zone_x = zone_x_positions[i]
            screen.blit(zone_image, (zone_x, top_margin))
            # Draw the black outlines
            pygame.draw.rect(screen, black, (zone_x, top_margin, 512, 512), 5)  # Width of 2 for the outline

            # Render and draw the label of the habitats
            label_text = font.render(zone_names[i], True, black)
            label_rect = label_text.get_rect()
            label_rect.centerx = spacing*(1+i) + zone_width*(1+i) - zone_width // 2
            label_rect.centery = top_margin - 20  # Adjust as needed
            screen.blit(label_text, label_rect)

            # Draw "Add Animals" button
            pygame.draw.rect(screen, black, add_button, 2)
            button_text = font.render("Add Animals", True, black)
            button_text_rect = button_text.get_rect(center=add_button.center)
            screen.blit(button_text, button_text_rect)

            # Draw zone button labels
            #button_label_text = f"Add {zone_names[i]}'s Animals"
            #button_label_font = pygame.font.Font(None, 36)
            #button_label_surface = button_label_font.render(button_label_text, True, (0, 0, 0))
            #button_label_rect = button_label_surface.get_rect(center=(zone_x + rectangle_width // 2, rectangle_y + button_height // 2))
            #screen.blit(button_label_surface, button_label_rect)

            # Draw food level indicator
            pygame.draw.rect(screen, white, (zone_x_positions[i], top_margin+habitat_height, habitat_width, foodIndicator_height))
            pygame.draw.rect(screen, (153,76,0), (zone_x_positions[i], top_margin+habitat_height, FoodLevels[i]*512//100, foodIndicator_height)) #Operation is made to scale the food value to the indicator
            pygame.draw.rect(screen, black, (zone_x_positions[i], top_margin+habitat_height, habitat_width, foodIndicator_height), 3)

            #Align the food level count
            food_count = font.render(f"{FoodLevels[i]}", True, white)
            food_count_rect = food_count.get_rect()
            food_count_rect.x = zone_x_positions[i] + 10 #Add a small margin
            food_count_rect.centery = top_margin+habitat_height+foodIndicator_height//2
            screen.blit(food_count, food_count_rect)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Draw animals inside their zone only if animals are added
        if animals_added:
            for current_zone in zone_names:
                zone_dict = {
                    "Forest": forest_animals,
                    "Savannah": savannah_animals,
                    "Tundra": tundra_animals
                }[current_zone]

                total_animals = len(zone_dict)
                max_columns = 2  # Maximum number of columns for animal display
                animal_width, animal_height = 150, 150  # Width and height of each animal image
                gap_x, gap_y = 50, 30  # Gap between animals in x and y directions
                columns = min(total_animals, max_columns)
                rows = (total_animals + max_columns - 1) // max_columns  # Calculate number of rows

                for index, (animal_name, animal_img) in enumerate(zone_dict.items()):
                    row = index // max_columns
                    column = index % max_columns

                    # Calculate animal positions based on the current zone
                    if current_zone == "Forest":
                        zone_x = forest_x
                    elif current_zone == "Savannah":
                        zone_x = savannah_x
                    elif current_zone == "Tundra":
                        zone_x = tundra_x


                    animal_x = zone_x + gap_x * (column + 1) + column * animal_width
                    animal_y = top_margin + gap_y * (row + 1) + row * animal_height
                    animal_rect = animal_img.get_rect(center=(animal_x + animal_width // 2, animal_y + animal_height // 2))

                    # Draw animal image
                    screen.blit(animal_img, animal_rect)

                    #Align the animal label with its sprite
                    animal_label = font.render(animal_name, True, white)
                    animal_label_rect = animal_label.get_rect()
                    animal_label_rect.x = animal_x
                    animal_label_rect.y = animal_y # Adjust as needed
                    screen.blit(animal_label, animal_label_rect)

                    # Iterate through the zoo's Zones and animals
                    for zone in myzoo.Zones:
                        for animal in zone.Animals:
                            health_level = animal.Health  # Access the Health attribute
                            # Use the 'health' value as needed in your code
                            # Draw health bar background
                            pygame.draw.rect(screen, red, (animal_x, animal_y - 10, healthbar_width, healthbar_height))
                            # Draw health bar
                            pygame.draw.rect(screen, green, (animal_x, animal_y - 10, health_level, healthbar_height))
                            # Draw a black outline for the health bar
                            pygame.draw.rect(screen, black, (animal_x, animal_y - 10, healthbar_width, healthbar_height), 2)
                    
                    # Draw animal image
                    screen.blit(animal_img, animal_rect)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
            #Draw zookeeper
            if employee_flag == False:
                zookeeper_rect = zookeeper_img_L.get_rect()
                zookeeper_rect.y = screen_height - 220  # Adjust as needed, make sure it does not overlap with the title or habitats
                zookeeper_rect.x = random.randint(spacing, screen_width-spacing - zookeeper_rect.width)
                employee_flag = True
            else:
                zookeeper_rect.x = zookeeper_rect.x + employee_speed

            employee_speed = wallBounce(zookeeper_rect.x, employee_speed, spacing, screen_width-spacing - zookeeper_rect.width)

            #Check the direction the employee is facing
            if employee_speed < 0:
                screen.blit(zookeeper_img_L, zookeeper_rect)  # Original direction
            elif employee_speed > 0:
                screen.blit(zookeeper_img_R, zookeeper_rect)  # Mirrored direction

            #Align the ID
            employee_ID = font.render(f"{myzoo.Employees[0].ID}", True, black)
            employee_ID_rect = employee_ID.get_rect()
            employee_ID_rect.x = zookeeper_rect.x + zookeeper_rect.width//2 #Add a small margin
            employee_ID_rect.y = zookeeper_rect.y-30 #Adjust as needed
            screen.blit(employee_ID, employee_ID_rect)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #Draw visitors
            for i in range(3):
                #Draw visitors
                visitor_rect = guy_img_L.get_rect()
                visitor_rect.y = 100  # Adjust as needed, make sure it does not overlap with the title or habitats
                visitor_rect.x = spacing + i*800
                
                #Check the direction the visitor is facing
                if visitor_speed < 0:
                    screen.blit(guy_img_L, visitor_rect)  # Original direction
                elif visitor_speed > 0:
                    screen.blit(guy_img_R, visitor_rect)  # Mirrored direction

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()