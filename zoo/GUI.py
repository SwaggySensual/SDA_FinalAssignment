import pygame
import sys

#Load the assets
savannah = pygame.image.load('assets/Savannah.png')
tundra = pygame.image.load('assets/Tundra.png')
forest = pygame.image.load('assets/Forest.png')
wolf = pygame.image.load('assets/wolf.png')
fox = pygame.image.load('assets/fox.png')
lion = pygame.image.load('assets/lion.png')
elephant = pygame.image.load('assets/elephant.png')
hyena = pygame.image.load('assets/hyena.png')
polarbear = pygame.image.load('assets/polarbear.png')


# Use pygame.transform.scale to scale down the image
savannah = pygame.transform.scale(savannah, (512, 512))
tundra = pygame.transform.scale(tundra, (512, 512))
forest = pygame.transform.scale(forest, (512, 512))

#Animals 
wolf = pygame.transform.scale(wolf, (150, 150))

#define colors
black = (0,0,0)
white = (255,255,255)

# Initialize pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 1920, 1080  # Full HD resolution

#Set object dimensions
button_width, button_height = 150, 25

# Define rectangle properties
rect_width = 512
rect_height = 512
spacing = 96  # Space between rectangles
top_margin = (screen_height - rect_height) // 2
left_rect_x = (screen_width - 3 * rect_width - 2 * spacing) // 2

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Create a font for labels
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 90)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    # Clear the screen (fill with black in this case)
    screen.fill((192, 192, 182))

    # Update other game logic or draw objects here

    # Define your title text
    title_text = "Zoo"
    title_text_surface = title_font.render(title_text, True, (0, 0, 0))
    
    # Get the rectangle for the title text
    text_rect = title_text_surface.get_rect()
    text_rect.centerx = screen_width // 2  # Center horizontally
    text_rect.centery = 50  # Adjust as needed for vertical position 

    # Blit the title text onto the screen
    screen.blit(title_text_surface, text_rect)

    # Labels for each habitat
    labels = ["Tundra", "Savannah", "Forest"]
    habitats = [tundra, savannah, forest]

    # Draw habitats
    # Draw rectangles
    for i in range(3):
        left = left_rect_x + i * (rect_width + spacing)
        # Create a Rect for the image
        image_rect = pygame.Rect(left, top_margin, rect_width, rect_height)
        screen.blit(habitats[i], image_rect)
        # Draw the black outlines
        pygame.draw.rect(screen, black, image_rect, 5)  # Width of 2 for the outline

        # Render and draw the label
        label_text = font.render(labels[i], True, black)
        label_rect = label_text.get_rect()
        label_rect.centerx = left + rect_width // 2
        label_rect.centery = top_margin - 50  # Adjust as needed
        screen.blit(label_text, label_rect)

    wolf_rect = pygame.Rect(screen_width-500, top_margin+100, 400, 400)
    screen.blit(wolf, wolf_rect)
    wolf_text = font.render('wolf', True, white)
    wolf_text_rect = wolf_text.get_rect()
    wolf_text_rect.centerx = screen_width-400
    wolf_text_rect.centery = top_margin+120  # Adjust as needed
    screen.blit(wolf_text, wolf_text_rect)
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()