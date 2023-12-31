

import pygame
import sys
import random

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
    "Artic fox" : pygame.image.load('assets/articfox.png'),
    "Black bear" : pygame.image.load('assets/blackbear.png'),
    "Cheetah" : pygame.image.load('assets/cheetah.png'),
    "Deer" : pygame.image.load('assets/deer.png'),
    "Ostrich" : pygame.image.load('assets/ostrich.png')

}

zookeeper_img = pygame.image.load('assets/zookeeper.png')


# Use pygame.transform.scale to scale down the images
savannah = pygame.transform.scale(savannah, (512, 512))
tundra = pygame.transform.scale(tundra, (512, 512))
forest = pygame.transform.scale(forest, (512, 512))

scaled_animal_images = {key: pygame.transform.scale(img, (130, 130)) for key, img in animal_images.items()}

zookeeper_img = pygame.transform.scale(zookeeper_img, (75, 130))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

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
    "Artic fox": scaled_animal_images["Artic fox"],
    "Polar bear": scaled_animal_images["Polar bear"]
}
# Define zone names
zone_names = ["Forest", "Savannah", "Tundra"]

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

# Main loop
running = True
current_zone = None
selected_animals = []  # Store selected animals for the current zone

while running:
   # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Check if any zone button is clicked
            for i, button_rect in enumerate(zone_buttons):
                if button_rect.collidepoint(mouse_pos):
                    current_zone = zone_names[i]  # Set the current zone based on the clicked button
                    selected_animals = list([forest_animals, savannah_animals, tundra_animals][i].keys())
                    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Clear the screen
    screen.fill((192, 192, 182))

    # Draw zoo title
    title_text = "ZOO"
    title_font = pygame.font.Font(None, 90)
    title_text_surface = title_font.render(title_text, True, (0, 0, 0))
    text_rect = title_text_surface.get_rect(center=(screen_width // 2, 50))
    screen.blit(title_text_surface, text_rect)

    #Draw zookeeper
    zookeeper_rect = zookeeper_img.get_rect()
    zookeeper_rect.x = spacing
    zookeeper_rect.y = 100  # Adjust as needed, make sure it does not overlap with the title or habitats
    screen.blit(zookeeper_img, zookeeper_rect)

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

     #Draw zone buttons
        pygame.draw.rect(screen, black, (zone_x, rectangle_y, rectangle_width, rectangle_height), 2)

     # Draw zone button labels
        button_label_text = f"Add {zone_names[i]}'s Animals"
        button_label_font = pygame.font.Font(None, 36)
        button_label_surface = button_label_font.render(button_label_text, True, (0, 0, 0))
        button_label_rect = button_label_surface.get_rect(center=(zone_x + rectangle_width // 2, rectangle_y + button_height // 2))
        screen.blit(button_label_surface, button_label_rect)


    # Draw animals inside their zone
    if current_zone is not None:
        zone_dict = [forest_animals, savannah_animals, tundra_animals][zone_names.index(current_zone)]
        total_animals = len(selected_animals)
        max_columns = 2  # Maximum number of columns for animal display
        animal_width, animal_height = 150, 150  # Width and height of each animal image
        gap_x, gap_y = 50, 30  # Gap between animals in x and y directions
        columns = min(total_animals, max_columns)
        rows = (total_animals + max_columns - 1) // max_columns  #Calculate number of rows
        
        for index, animal_name in enumerate(selected_animals):
            row = index // max_columns
            column = index % max_columns
            animal_img = zone_dict[animal_name]
            animal_x = zone_x_positions[zone_names.index(current_zone)] + gap_x * (column + 1) + column * animal_width
            animal_y = top_margin + gap_y * (row + 1) + row * animal_height
            animal_rect = animal_img.get_rect(center=(animal_x + animal_width // 2, animal_y + animal_height // 2))

            #Align the animal label with its sprite
            animal_label = font.render(animal_name, True, white)
            animal_label_rect = animal_label.get_rect()
            animal_label_rect.x = animal_x
            animal_label_rect.y = animal_y # Adjust as needed
            screen.blit(animal_label, animal_label_rect)

            # Calculate health bar width based on animal's health
            health_percentage = animal_health[animal_name] / 100
            health_level = int(healthbar_width * health_percentage)

            # Draw health bar background
            pygame.draw.rect(screen, red, (animal_x, animal_y - 10, healthbar_width, healthbar_height))
            # Draw health bar
            pygame.draw.rect(screen, green, (animal_x, animal_y - 10, health_level, healthbar_height))
            # Draw a black outline for the health bar
            pygame.draw.rect(screen, black, (animal_x, animal_y - 10, healthbar_width, healthbar_height), 2)
            
            # Draw animal image
            screen.blit(animal_img, animal_rect)

           


    

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()