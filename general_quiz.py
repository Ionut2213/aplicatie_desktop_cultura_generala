import pygame
import sys
from new_general_quiz_game import run_new_game
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

    selected_difficulty = None
    show_difficulty_menu = False

    def draw_difficulty_menu(mouse_pos):
        nonlocal selected_difficulty

        dropdown_width, dropdown_height = 300, 60
        dropdown_x = screen_width // 2 - dropdown_width // 2
        dropdown_y_start = screen_height // 2 + 100
        options = ["Easy", "Medium", "Hard"]

        for i, option in enumerate(options):
            dropdown_y = dropdown_y_start + i * dropdown_height
            if dropdown_x < mouse_pos[0] < dropdown_x + dropdown_width and dropdown_y < mouse_pos[1] < dropdown_y + dropdown_height:
                option_color = dark_grey
            else:
                option_color = grey

            pygame.draw.rect(screen, option_color, (dropdown_x, dropdown_y, dropdown_width, dropdown_height))
            pygame.draw.rect(screen, black, (dropdown_x, dropdown_y, dropdown_width, dropdown_height), 2)
            option_text = font_button.render(option, True, black)
            screen.blit(option_text, (dropdown_x + dropdown_width // 2 - option_text.get_width() // 2, dropdown_y + dropdown_height // 2 - option_text.get_height() // 2))

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
                button_width, button_height = 300, 80
                button_x = screen_width // 2 - button_width // 2
                button_y_start = screen_height // 2 - 100
                button_gap = 20

                new_game_button_y = button_y_start
                if button_x < mouse_pos[0] < button_x + button_width and new_game_button_y < mouse_pos[1] < new_game_button_y + button_height:
                    run_new_game()

                change_difficulty_button_y = button_y_start + button_height + button_gap
                if button_x < mouse_pos[0] < button_x + button_width and change_difficulty_button_y < mouse_pos[1] < change_difficulty_button_y + button_height:
                    show_difficulty_menu = not show_difficulty_menu

                back_to_menu_button_y = change_difficulty_button_y + button_height + button_gap
                if button_x < mouse_pos[0] < button_x + button_width and back_to_menu_button_y < mouse_pos[1] < back_to_menu_button_y + button_height:
                    running = False

                if show_difficulty_menu:
                    dropdown_width, dropdown_height = 300, 60
                    dropdown_x = screen_width // 2 - dropdown_width // 2
                    dropdown_y_start = screen_height // 2 + 100
                    options = ["Easy", "Medium", "Hard"]

                    for i, option in enumerate(options):
                        dropdown_y = dropdown_y_start + i * dropdown_height
                        if dropdown_x < mouse_pos[0] < dropdown_x + dropdown_width and dropdown_y < mouse_pos[1] < dropdown_y + dropdown_height:
                            selected_difficulty = option
                            show_difficulty_menu = False
                            print(f"Selected difficulty: {selected_difficulty}")

        screen.fill(white)

        button_width, button_height = 300, 80
        button_x = screen_width // 2 - button_width // 2
        button_y_start = screen_height // 2 - 100
        button_gap = 20

        buttons = ["New Game", "Change difficulty", "Main Menu"]

        for i, button_text in enumerate(buttons):
            button_y = button_y_start + i * (button_height + button_gap)
            if button_x < mouse_pos[0] < button_x + button_width and button_y < mouse_pos[1] < button_y + button_height:
                button_color = dark_grey
            else:
                button_color = grey

            pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
            pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height), 2)
            button_text_rendered = font_button.render(button_text, True, black)
            screen.blit(button_text_rendered, (button_x + button_width // 2 - button_text_rendered.get_width() // 2,
                                               button_y + button_height // 2 - button_text_rendered.get_height() // 2))

        if show_difficulty_menu:
            draw_difficulty_menu(mouse_pos)

        pygame.display.flip()

    pygame.quit()
    sys.exit()