import pygame
import sys

pygame.init()


screen_info = pygame.display.Info()
screen_widht = screen_info.current_w
screen_height = screen_info.current_h


screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption("New Game")

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 48)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)


questions = [
    {"question" : "What is the highest waterfall in the world?",
     "options": ["a) Niagara Falls", "b) Victoria Falls", "c) Angel Falls"], "correct": "c"}
    
   
]

def run_new_game():
    current_question = 0
    score = 0
    total_questions = len(questions)
    max_wrong_answers = 3
    wrong_answers = 0
    question_time = 30
    time_left = question_time
    start_time = pygame.time.get_ticks()


    def display_message(text, font, color, center):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=center)
        screen.blit(text_surface, text_rect)

    running = True
    while running:
        screen.fill(white)


        if current_question < total_questions and wrong_answers < max_wrong_answers:
            question = questions[current_question]
            display_message(question["question"], big_font, black, (screen_widht // 2, 100))

            for i, option in enumerate(question["options"]):
                display_message(option, font, blue, (screen_widht // 2, 200 + i * 40))

            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
            time_left = max(question_time - elapsed_time, 0)

            time_color = red if time_left < 10 else black
            display_message(f"Time left: {int(time_left)} seconds", font, time_color, (screen_widht // 2, 600))

            if time_left <= 0:
                wrong_answers += 1
                start_time = pygame.time.get_ticks()
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        answer = 'a'
                    elif event.key == pygame.K_b:
                        answer = 'b'
                    elif event.key == pygame.K_c:
                        answer = 'c'
                    else:
                        answer = ''
                    
                    if answer == question['correct']:
                        score += 1
                    else:
                        wrong_answers += 1
                        current_question += 1
                        start_time = pygame.time.get_ticks()

        else:
            if wrong_answers >= max_wrong_answers:
                display_message("Game Over", big_font, black, (screen_widht // 2, 200))
            else:
                display_message(f"You answered correctly to {score} questions!", big_font, black, (screen_widht // 2, 200))
                display_message(f"You scored {score / total_questions * 100:.2f}%.", big_font, black, (screen_widht // 2, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()
                
