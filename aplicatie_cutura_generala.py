import pygame  # if you don't have pygame installed use the command pip install pygame
import sys

# Fonts and color part
font_title = pygame.font.Font(None, 70)
font_button = pygame.font.Font(None, 45)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 102, 204)
grey = (200, 200, 200)
dark_grey = (150, 150, 150)

# Main window of the app
pygame.init()

# Automatically detect the screen resolution of the user's display
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("General Knowledge Application")










def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
