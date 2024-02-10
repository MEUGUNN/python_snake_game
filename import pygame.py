import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Set the clock
clock = pygame.time.Clock()

# Set the font
font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    """
    Display a message on the screen.
    """
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])


def gameLoop():
    """
    Main game loop.
    """
    game_over = False
    game_close = False

    # Initial position of the snake
    x_snake = screen_width / 2
    y_snake = screen_height / 2

    # Initial velocity of the snake
    x_snake_change = 0
    y_snake_change = 0

    # Length of the snake
    snake_list = []
    snake_length = 1

    # Initial position of the food
    x_food = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
    y_food = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill(blue)
            message("You lost! Press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_snake_change = -10
                    y_snake_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_snake_change = 10
                    y_snake_change = 0
                elif event.key == pygame.K_UP:
                    y_snake_change = -10
                    x_snake_change = 0
                elif event.key == pygame.K_DOWN:
                    y_snake_change = 10
                    x_snake_change = 0

        if x_snake >= screen_width or x_snake < 0 or y_snake >= screen_height or y_snake < 0:
            game_close = True
        x_snake += x_snake_change
        y_snake += y_snake_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [x_food, y_food, 10, 10])

        snake_head = []
        snake_head.append(x_snake)
        snake_head.append(y_snake)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(screen, black, [segment[0], segment[1], 10, 10])

        pygame.display.update()

        if x_snake == x_food and y_snake == y_food:
            x_food = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
            y_food = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0
            snake_length += 1

        clock.tick(30)

    pygame.quit()
    quit()


# Start the game loop
gameLoop()
