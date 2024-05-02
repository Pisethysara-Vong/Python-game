import pygame
import sys
import random
import json

pygame.init()
window_width = 500
window_height = 750
# draw window
game_screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Rising Slime")
font = pygame.font.Font(None, 40)


# define player class
class Player:
    def __init__(self):
        self.body_x = 235
        self.body_y = 675
        self.body_size = 15
        self.player_speed = 5

    def draw_player(self):
        player = pygame.Rect(self.body_x, self.body_y, self.body_size, self.body_size)
        pygame.draw.rect(game_screen, (0, 255, 0), player)


# define obstacle class
class Obstacles:
    def __init__(self, num1, num2, num3, num4):
        self.obstacle_x = random.randint(num3, num4)
        self.obstacle_y = random.randint(num1, num2)
        self.obstacle_width = 45
        self.obstacle_height = 5

    def draw_obstacle(self):
        obstacle_rect = pygame.Rect(self.obstacle_x, self.obstacle_y, self.obstacle_width, self.obstacle_height)
        pygame.draw.rect(game_screen, (255, 255, 255), obstacle_rect)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


# Main container function that holds the buttons and game functions
def start_page():
    def move_obstacles(value):
        obstacle1.obstacle_y += value
        obstacle2.obstacle_y += value
        obstacle3.obstacle_y += value
        obstacle4.obstacle_y += value
        obstacle5.obstacle_y += value
        obstacle6.obstacle_y += value
        obstacle7.obstacle_y += value
        obstacle8.obstacle_y += value
        obstacle9.obstacle_y += value
        obstacle10.obstacle_y += value

    def new_obstacle(obsNum, x, y):
        if obsNum.obstacle_y + obsNum.obstacle_height > 750:
            obsNum.obstacle_x = random.randint(x, y)
            obsNum.obstacle_y = 0

    obstacle1 = Obstacles(25, 70, 0, 230)
    obstacle2 = Obstacles(95, 140, 235, 455)
    obstacle3 = Obstacles(165, 210, 0, 230)
    obstacle4 = Obstacles(235, 280, 235, 455)
    obstacle5 = Obstacles(305, 350, 0, 230)
    obstacle6 = Obstacles(375, 420, 235, 455)
    obstacle7 = Obstacles(445, 490, 0, 230)
    obstacle8 = Obstacles(515, 560, 235, 455)
    obstacle9 = Obstacles(585, 630, 0, 230)
    obstacle10 = Obstacles(655, 700, 235, 455)

    while True:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        game_screen.fill((0, 0, 0))

        obstacle1.draw_obstacle()
        obstacle2.draw_obstacle()
        obstacle3.draw_obstacle()
        obstacle4.draw_obstacle()
        obstacle5.draw_obstacle()
        obstacle6.draw_obstacle()
        obstacle7.draw_obstacle()
        obstacle8.draw_obstacle()
        obstacle9.draw_obstacle()
        obstacle10.draw_obstacle()

        move_obstacles(3)

        new_obstacle(obstacle1, 0, 230)
        new_obstacle(obstacle2, 235, 455)
        new_obstacle(obstacle3, 0, 230)
        new_obstacle(obstacle4, 235, 455)
        new_obstacle(obstacle5, 0, 230)
        new_obstacle(obstacle6, 235, 455)
        new_obstacle(obstacle7, 0, 230)
        new_obstacle(obstacle8, 235, 455)
        new_obstacle(obstacle9, 0, 230)
        new_obstacle(obstacle10, 235, 455)

        draw_text('Rising Slime', pygame.font.Font(None, 80), (0, 255, 0), game_screen, 88, 120)
        x_mouse_pos, y_mouse_pos = pygame.mouse.get_pos()
        # creating buttons
        button_1 = pygame.Rect(150, 400, 200, 50)
        button_2 = pygame.Rect(150, 500, 200, 50)
        # defining functions when a certain button is pressed
        if button_1.collidepoint((x_mouse_pos, y_mouse_pos)):
            if click:
                game()
        elif button_2.collidepoint((x_mouse_pos, y_mouse_pos)):
            if click:
                how_to_play()
        pygame.draw.rect(game_screen, (0, 255, 0), button_1)
        pygame.draw.rect(game_screen, (0, 255, 0), button_2)
        # writing text on top of button
        draw_text('PLAY', font, (0, 0, 0), game_screen, 215, 413)
        draw_text('How To Play', font, (0, 0, 0), game_screen, 168, 513)
        pygame.display.update()
        clock.tick(60)


def game():
    def draw_game_over():
        game_screen.fill((0, 0, 0))
        with open("Hi-score_holder.txt") as holder:
            name = json.load(holder)
        game_over_text = pygame.font.Font(None, 75).render("Game Over", True, (255, 0, 0))
        game_screen.blit(game_over_text, (110, 70))
        final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
        game_screen.blit(final_score_text, (150, 200))
        high_score_text = font.render("Hi-Score: " + str(high_score) + " set by " + str(name), True, (255, 255, 255))
        game_screen.blit(high_score_text, (80, 240))
        draw_text("Press SPACE to play again!", font, (255, 255, 255), game_screen, 70, 400)
        x_mouse_pos, y_mouse_pos = pygame.mouse.get_pos()
        # creating buttons
        button_2 = pygame.Rect(150, 450, 200, 50)
        pygame.draw.rect(game_screen, (0, 255, 0), button_2)
        # writing text on top of button
        draw_text('Menu', font, (0, 0, 0), game_screen, 215, 463)
        if click is True:
            if button_2.collidepoint((x_mouse_pos, y_mouse_pos)):
                start_page()

    def game_over_hiscore():
        input_box = pygame.Rect(280, 317, 140, 32)
        button_2 = pygame.Rect(150, 450, 200, 50)
        color_inactive = pygame.Color('white')
        color_active = pygame.Color((0, 255, 0))
        color = color_inactive
        active = False
        text = ''
        done = False
        username = ''
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    elif button_2.collidepoint(event.pos) and username != '':
                        start_page()
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            username = text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            key = pygame.key.get_pressed()
            if username == '':
                game_screen.fill((0, 0, 0))
                txt_surface = font.render(text, True, 'white')
                # Resize the box if the text is too long.
                width = max(200, txt_surface.get_width() + 10)
                input_box.w = width
                # Blit the text.
                game_screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                # Blit the input_box rect.
                pygame.draw.rect(game_screen, color, input_box, 2)
                game_over_text = pygame.font.Font(None, 75).render("Game Over", True, (255, 0, 0))
                game_screen.blit(game_over_text, (110, 70))
                final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
                game_screen.blit(final_score_text, (150, 200))
                high_score_text = font.render("Hi-Score: " + str(high_score) + " set by " + str(username), True,
                                              (255, 255, 255))
                game_screen.blit(high_score_text, (80, 240))
                draw_text("You have set a new Hi-Score!", font, (255, 255, 255), game_screen, 40, 280)
                draw_text("Enter a username: ", font, (255, 255, 255), game_screen, 20, 320)
            elif username != '':
                with open('Hi-score_holder.txt', 'w') as holder:
                    json.dump(username, holder)
                draw_game_over()
            if username != '' and key[pygame.K_SPACE]:
                game()
            pygame.display.flip()
            clock.tick(60)

    def move_obstacles(value):
        obstacle1.obstacle_y += value
        obstacle2.obstacle_y += value
        obstacle3.obstacle_y += value
        obstacle4.obstacle_y += value
        obstacle5.obstacle_y += value
        obstacle6.obstacle_y += value
        obstacle7.obstacle_y += value
        obstacle8.obstacle_y += value
        obstacle9.obstacle_y += value
        obstacle10.obstacle_y += value

    def new_obstacle(obsNum, x, y):
        if obsNum.obstacle_y + obsNum.obstacle_height > 750:
            obsNum.obstacle_x = random.randint(x, y)
            obsNum.obstacle_y = 0
            return True

    def collision(obsNum):
        if (player.body_x < obsNum.obstacle_x + obsNum.obstacle_width and
                player.body_x + player.body_size > obsNum.obstacle_x and
                player.body_y < obsNum.obstacle_y + obsNum.obstacle_height and
                player.body_y + player.body_size > obsNum.obstacle_y):
            return True

    obstacle1 = Obstacles(25, 70, 0, 230)
    obstacle2 = Obstacles(95, 140, 235, 455)
    obstacle3 = Obstacles(165, 210, 0, 230)
    obstacle4 = Obstacles(235, 280, 235, 455)
    obstacle5 = Obstacles(305, 350, 0, 230)
    obstacle6 = Obstacles(375, 420, 235, 455)
    obstacle7 = Obstacles(445, 490, 0, 230)
    obstacle8 = Obstacles(515, 560, 235, 455)
    obstacle9 = Obstacles(585, 630, 0, 230)
    obstacle10 = Obstacles(655, 700, 235, 455)

    # create player variable
    player = Player()
    score = 0
    high_score = 0
    with open('scoreboard.txt') as scoreboard:
        high_score = json.load(scoreboard)
    running = True
    game_over = False

    while running:
        clock.tick(60)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.body_x -= player.player_speed
        if keys[pygame.K_RIGHT]:
            player.body_x += player.player_speed
        game_screen.fill((0, 0, 0))
        if player.body_x >= 485:
            player.body_x = 485
        elif player.body_x <= 0:
            player.body_x = 0

        obstacle1.draw_obstacle()
        obstacle2.draw_obstacle()
        obstacle3.draw_obstacle()
        obstacle4.draw_obstacle()
        obstacle5.draw_obstacle()
        obstacle6.draw_obstacle()
        obstacle7.draw_obstacle()
        obstacle8.draw_obstacle()
        obstacle9.draw_obstacle()
        obstacle10.draw_obstacle()
        player.draw_player()

        move_obstacles(3)

        if collision(obstacle1):
            game_over = True
        if collision(obstacle2):
            game_over = True
        if collision(obstacle3):
            game_over = True
        if collision(obstacle4):
            game_over = True
        if collision(obstacle5):
            game_over = True
        if collision(obstacle6):
            game_over = True
        if collision(obstacle7):
            game_over = True
        if collision(obstacle8):
            game_over = True
        if collision(obstacle9):
            game_over = True
        if collision(obstacle10):
            game_over = True

        if new_obstacle(obstacle1, 0, 230):
            score += 1
        new_obstacle(obstacle2, 235, 455)
        new_obstacle(obstacle3, 0, 230)
        if new_obstacle(obstacle4, 235, 455):
            score += 1
        new_obstacle(obstacle5, 0, 230)
        new_obstacle(obstacle6, 235, 455)
        if new_obstacle(obstacle7, 0, 230):
            score += 1
        new_obstacle(obstacle8, 235, 455)
        new_obstacle(obstacle9, 0, 230)
        if new_obstacle(obstacle10, 235, 455):
            score += 1

        if high_score < score:
            high_score = score

        if 11 <= score <= 25:
            move_obstacles(2)
        if 26 <= score <= 40:
            player.player_speed = 6
            move_obstacles(4)
        if 41 <= score <= 55:
            player.player_speed = 7
            move_obstacles(6)
        if 56 <= score <= 80:
            player.player_speed = 8
            move_obstacles(8)
        if 81 <= score:
            player.player_speed = 10
            move_obstacles(10)

        text = font.render("Score: " + str(score), True, (255, 255, 255))
        game_screen.blit(text, (10, 10))
        text = font.render("Hi-Score: " + str(high_score), True, (255, 255, 255))
        game_screen.blit(text, (10, 40))

        if game_over is True:
            obstacle1.obstacle_y = 0
            obstacle2.obstacle_y = 0
            obstacle3.obstacle_y = 0
            obstacle4.obstacle_y = 0
            obstacle5.obstacle_y = 0
            obstacle6.obstacle_y = 0
            obstacle7.obstacle_y = 0
            obstacle8.obstacle_y = 0
            obstacle9.obstacle_y = 0
            obstacle10.obstacle_y = 0
            with open('scoreboard.txt', 'w') as scoreboard:
                json.dump(high_score, scoreboard)
            if high_score == score:
                game_over_hiscore()
            else:
                draw_game_over()

        if keys[pygame.K_SPACE] and game_over:
            game_over = False
            obstacle1 = Obstacles(25, 70, 0, 230)
            obstacle2 = Obstacles(95, 140, 235, 455)
            obstacle3 = Obstacles(165, 210, 0, 230)
            obstacle4 = Obstacles(235, 280, 235, 455)
            obstacle5 = Obstacles(305, 350, 0, 230)
            obstacle6 = Obstacles(375, 420, 235, 455)
            obstacle7 = Obstacles(445, 490, 0, 230)
            obstacle8 = Obstacles(515, 560, 235, 455)
            obstacle9 = Obstacles(585, 630, 0, 230)
            obstacle10 = Obstacles(655, 700, 235, 455)
            # create player variable
            player = Player()
            score = 0
            high_score = 0
            with open('scoreboard.txt') as scoreboard:
                high_score = json.load(scoreboard)

        pygame.display.flip()
    pygame.quit()


def how_to_play():
    running = True
    while running:
        clock.tick(60)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        game_screen.fill((0, 0, 0))
        draw_text("Press the <- key and -> key to move", font, (255, 255, 255), game_screen, 8, 200)
        draw_text("the slime and avoid the obstacles.", font, (255, 255, 255), game_screen, 25, 250)
        x_mouse_pos, y_mouse_pos = pygame.mouse.get_pos()
        back_button = pygame.Rect(150, 400, 200, 50)
        if back_button.collidepoint((x_mouse_pos, y_mouse_pos)):
            if click:
                start_page()
        pygame.draw.rect(game_screen, (0, 255, 0), back_button)
        # writing text on top of button
        draw_text('Back', font, (0, 0, 0), game_screen, 215, 413)
        pygame.display.flip()


start_page()
