import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen dimensions (Full HD)
screen_width, screen_height = 1920, 1080

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Define rectangle properties
rect_width = 512
rect_height = 512
spacing = 50  # Space between rectangles
top_margin = (screen_height - rect_height) // 2
left_rect_x = (screen_width - 3 * rect_width - 2 * spacing) // 2

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create a font for labels
font = pygame.font.Font(None, 36)

# Labels for each rectangle
labels = ["Rectangle A", "Rectangle B", "Rectangle C"]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Clear the screen
    screen.fill(white)

    # Draw rectangles
    for i in range(3):
        left = left_rect_x + i * (rect_width + spacing)
        pygame.draw.rect(screen, black, (left, top_margin, rect_width, rect_height))

        # Render and draw the label
        label_text = font.render(labels[i], True, black)
        label_rect = label_text.get_rect()
        label_rect.centerx = left + rect_width // 2
        label_rect.centery = top_margin - 50  # Adjust as needed
        screen.blit(label_text, label_rect)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()