import pygame  # if you don't have pygame installed use the command pip install pygame
import sys
from general_quiz import general_quiz_app

# Main window of the app
pygame.init()



# Automatically detect the screen resolution of the user's display
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("General Knowledge Application")



# Fonts and color part
font_title = pygame.font.Font(None, 72)
font_button = pygame.font.Font(None, 48)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 102, 204)
grey = (200, 200, 200)
dark_grey = (150, 150, 150)

dropdown_open = False
selected_difficulty = None
show_difficulty_menu = False




def draw_main_screen(mouse_pos):
    screen.fill(white)
    # Title
    title_text = font_title.render("Welcome!!", True, blue)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 4))


    # Buttons

    button_width, button_height = 300, 80
    button_x = screen_width // 2 - button_width // 2
    button_y_start = screen_height // 2
    button_gap = 20

    buttons = ["General Quiz", "Guess the flag", "To be added"]

    for i, button_text in enumerate(buttons):
        button_y = button_y_start + i * (button_height + button_gap)
        # Mouse position over the buttons
        if button_x < mouse_pos[0] < button_x + button_width and button_y < mouse_pos[1] < button_y + button_height:
            button_color = dark_grey
        else:
            button_color = grey

        pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
        pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height), 2)
        button_text_rendered = font_button.render(button_text, True, black)
        screen.blit(button_text_rendered, (button_x + button_width // 2 - button_text_rendered.get_width() // 2, 
                                           button_y + button_height // 2 - button_text_rendered.get_height() // 2))
    if selected_difficulty:
        difficulty_text = font_button.render(f"Selected difficulty: {selected_difficulty}", True, blue)
        screen.blit(difficulty_text, (screen_width // 2 - difficulty_text.get_width() // 2, screen_height // 1.2))






def draw_dropdown_menu(mouse_pos):
    dropdown_widht, dropdown_height = 300, 60
    dropdown_x = screen_width // 2 - dropdown_widht // 2
    dropdown_y_start = screen_height // 2 + 100
    options = ["Easy", "Medium", "Hard"]

    for i, option in enumerate(options):
        dropdown_y = dropdown_y_start + i * dropdown_height
        if dropdown_x < mouse_pos[0] < dropdown_x + dropdown_widht and dropdown_y < mouse_pos[1] < dropdown_y + dropdown_height:
            option_color = dark_grey
        else:
            option_color = grey

        pygame.draw.rect(screen, option_color, (dropdown_x, dropdown_y, dropdown_widht, dropdown_height))
        pygame.draw.rect(screen, black, (dropdown_x, dropdown_y, dropdown_widht, dropdown_height), 2)
        option_text = font_button.render(option, True, black)
        screen.blit(option_text, (dropdown_x + dropdown_widht // 2 - option_text.get_width() // 2, dropdown_y + dropdown_height // 2 - option_text.get_height() // 2))

    if selected_difficulty:
        difficulty_text = font_button.render(f"Selected difficulty: {selected_difficulty}", True, blue)
        screen.blit(difficulty_text, (screen_width // 2 - difficulty_text.get_width() // 2, screen_height // 1.2))


def main():
    global dropdown_open, selected_difficulty, show_difficulty_menu
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
                button_y_start = screen_height // 2
                button_gap = 20

                general_quiz_button_y = button_y_start
                if button_x < mouse_pos[0] < button_x + button_width and general_quiz_button_y < mouse_pos[1] < general_quiz_button_y + button_height:
                    show_difficulty_menu = not show_difficulty_menu
                    print("Button 'General Quiz' was pressed")
                    general_quiz_app()

                
                guess_the_flag_button_y = button_y_start
                if button_x < mouse_pos[0] < button_x + button_width and guess_the_flag_button_y < mouse_pos[1] < guess_the_flag_button_y + button_height:
                    print("Button 'Guess the flag' was pressed")

                to_be_added_button_y = button_y_start
                if button_x < mouse_pos[0] < button_x + button_width and to_be_added_button_y < mouse_pos[1] < to_be_added_button_y + button_height:
                    print("Button 'to be added ' was pressed")
                
                if show_difficulty_menu:
                    dropdown_widht, dropdown_height = 300, 60
                    dropdown_x = screen_width // 2 - dropdown_widht // 2
                    dropdown_y_start = screen_height // 2 + 100
                    options = ["Easy", "Medium", "Hard"]

                    for i, option in enumerate(options):
                        dropdown_y = dropdown_y_start + i * dropdown_height
                        if dropdown_x < mouse_pos[0] < dropdown_x + dropdown_widht and dropdown_y < mouse_pos[1] < dropdown_y + dropdown_height:
                            selected_difficulty = option
                            show_difficulty_menu = False
                            print(f"The selected difficulty : {selected_difficulty}")


        if show_difficulty_menu:
            draw_dropdown_menu(mouse_pos)
        else:
            draw_main_screen(mouse_pos)

        pygame.display.flip()

    pygame.quit()
    sys.exit()      


if __name__ == "__main__":
    main()
