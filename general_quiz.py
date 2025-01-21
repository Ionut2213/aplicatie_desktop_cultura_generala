import pygame
import sys


def general_quiz_app():
    pygame.init()

    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("General Quiz")


    font_button = pygame.font.Font(None, 48)
    white = (255, 255, 255)
    black = (0, 0, 0)
    grey = (200, 200, 200)
    dark_grey = (150, 150, 150)

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_widht, button_height = 300, 80
                button_x = screen_width // 2 - button_widht // 2
                button_y_start = screen_height // 2
                button_gap = 20

                new_game_button_y = button_y_start
                if button_x < mouse_pos[0] < button_x and new_game_button_y < mouse_pos[1] < new_game_button_y + button_height:
                    print("New Game Button was pressed")

                change_difficulty_button_y = button_y_start + button_height + button_gap
                if button_x < mouse_pos[0] < button_x and change_difficulty_button_y < mouse_pos[1] < change_difficulty_button_y + button_height:
                    print("Change Button difficulty was pressed")

                back_to_menu_button_y = change_difficulty_button_y + button_height + button_gap
                if button_x < mouse_pos[0] < button_x + button_widht and back_to_menu_button_y < mouse_pos[1] < back_to_menu_button_y + button_height:
                    running = False
        
        screen.fill(white)

        button_widht, button_height = 300, 80
        button_x = screen_width // 2 - button_widht // 2
        button_y_start = screen_height // 2 - 100
        button_gap = 20

        buttons = ["New Game", "Change difficulty", "Main Menu"]

        for i, button_text in enumerate(buttons):
            button_y = button_y_start + i * (button_height + button_gap)
            if button_x < mouse_pos[0] < button_x + button_widht and button_y < mouse_pos[1] < button_y + button_height:
                button_color = dark_grey
            else:
                button_color = grey

            pygame.draw.rect(screen, button_color, (button_x, button_y, button_widht, button_height))
            pygame.draw.rect(screen, black, (button_x, button_y, button_widht, button_height), 2)
            button_text_rendered = font_button.render(button_text, True, black)
            screen.blit(button_text_rendered, (button_x + button_widht // 2 - button_text_rendered.get_width() // 2,
                                               button_y + button_height // 2 - button_text_rendered.get_height() // 2))
        
        pygame.display.flip()
    pygame.quit()
    sys.exit()