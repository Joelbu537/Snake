import pygame
import random
from enum import Enum

class GameFieldObjectType(Enum):
    EMPTY = 0
    SNAKE = 1
    FOOD = 2
    HEAD = 3

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    NONE = 4

class GameFieldObject:
    def __init__(self, x, y, typ, direction):
        self.x = x
        self.y = y
        self.typ = typ
        self.direction = direction

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
gameField = [
    [GameFieldObject(x, y, GameFieldObjectType.EMPTY, Direction.NONE) for x in range(30)]
    for y in range(18)
]
snake = [Coordinates(10, 10), Coordinates(9, 10), Coordinates(8, 10)]
def new_food():
    is_valid = False
    global gameField
    global snake
    global foodCoords
    temp_coords = Coordinates(0, 0)
    while not is_valid:
        temp_coords = Coordinates(random.randint(0, 29), random.randint(0, 17))
        is_valid = True
        for i in range(0, len(snake) - 1, 1):
            if temp_coords.x == snake[i].x and temp_coords.y == snake[i].y:
                is_valid = False
    print("Food set to " + str(temp_coords.x) + " " + str(temp_coords.y))
    return temp_coords


foodCoords = new_food()
playerDirection = Direction.RIGHT
alive = True
ate_food = False
score = 0
pygame.mixer.init(frequency=22050, size=-16, channels=16, buffer=4096)
food_sound = pygame.mixer.Sound("sounds\\food.mp3")
move_sound = pygame.mixer.Sound("sounds\\move.mp3")
head_position = Coordinates(-1, -1)


def handle_input():
    global playerDirection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and playerDirection != Direction.DOWN:
        playerDirection = Direction.UP
    elif keys[pygame.K_s] and playerDirection != Direction.UP:
        playerDirection = Direction.DOWN
    elif keys[pygame.K_a] and playerDirection != Direction.RIGHT:
        playerDirection = Direction.LEFT
    elif keys[pygame.K_d] and playerDirection != Direction.LEFT:
        playerDirection = Direction.RIGHT

def update_game_logic():
    #  Gehirn benutzen!!!
    global foodCoords
    global gameField

    # Snake bewegen
    print("The Snake is " + str(len(snake)) + " long")
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = Coordinates(snake[i - 1].x, snake[i - 1].y)


    # Kopf bewegen
    vector = Coordinates(0, 0)
    if playerDirection == Direction.UP:
        vector = Coordinates(0, -1)
    elif playerDirection == Direction.DOWN:
        vector = Coordinates(0, 1)
    elif playerDirection == Direction.LEFT:
        vector = Coordinates(-1, 0)
    elif playerDirection == Direction.RIGHT:
        vector = Coordinates(1, 0)
    global head_position
    head_position = Coordinates(snake[0].x + vector.x, snake[0].y + vector.y)
    global alive
    if head_position.x < 0 or head_position.x >= 30 or head_position.y < 0 or head_position.y >= 18:
        alive = False
    else:
        print("Moving head from (" + str(snake[0].x) + "|" + str(snake[0].y) + ") ", end="")
        snake[0] = head_position
        print("to (" + str(snake[0].x) + "|" + str(snake[0].y) + ")")
        move_sound.play()

def main():
    global playerDirection
    pygame.init()
    screen = pygame.display.set_mode((1200, 780))
    pygame.display.set_caption("Snake")
    pygame.mouse.set_visible(True)
    font = pygame.font.SysFont(None, 48)
    death_font = pygame.font.SysFont(None, 150)

    clock = pygame.time.Clock()
    running = True

    logic_timer = 0
    logic_interval = 3 / len(snake)  # Updates/Sekunde, vielleicht 90° Parabel oder so?

    start_time = pygame.time.get_ticks()
    game_music = pygame.mixer.Sound("sounds\\music.mp3")
    food_image = pygame.image.load("images\\apple.png")
    foodrect = food_image.get_rect()
    game_music.play(loops=-1)
    global alive
    time_text = ""
    while running:
        dt = clock.tick(60) / 1000  # 60 FPS
        if (2 - (0.15*len(snake))) > 0.15:
            logic_interval = 1.6 - (0.15*len(snake))
        else:
            logic_interval = 0.15
        logic_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if alive:
            handle_input()  # Läuft mit 60 FPS

        if logic_timer >= logic_interval and alive:
            update_game_logic()
            logic_timer = 0  # Reset Timer

        global ate_food
        if ate_food:
            new_snake_element = snake[len(snake) - 1]
            ate_food = False
        else:
            new_snake_element = Coordinates(-1, 0)

        if new_snake_element.x != -1:
            snake.append(new_snake_element)

        # Food prüfend
        global foodCoords
        if snake[0].x == foodCoords.x and snake[0].y == foodCoords.y:
            global food_sound
            food_sound.play()
            print("Ate food")
            global score
            score += 1
            ate_food = True
            foodCoords = new_food()

        global head_position
        for i in range(1, len(snake), 1):
            if snake[i].x == head_position.x and snake[i].y == head_position.y:
                print("Hit")
                alive = False

        # Fenster füllen
        screen.fill("black")
        pygame.draw.rect(screen, "white", (0, 0, 1200, 60), 0)

        score_text = font.render("Score:  " + str(len(snake) - 3), True, (0, 0, 0))
        time_in_seconds = (pygame.time.get_ticks() - start_time) // 1000
        time_formatted = "Time:  " + str(time_in_seconds // 60)
        if not (time_in_seconds % 60) >= 10:
            time_formatted += ":0" + str(time_in_seconds % 60)
        else:
            time_formatted += ":" + str(time_in_seconds % 60)
        if alive:
            time_text = font.render(time_formatted, True, (0, 0, 0)) # Kann 0:2 anzeigen, muss gefixt werden
        screen.blit(score_text, (1000, 12))
        screen.blit(time_text, (50, 12))

        foodrect.x = foodCoords.x * 40
        foodrect.y = foodCoords.y * 40
        screen.blit(food_image, foodrect)
        #pygame.draw.rect(screen, "green", (foodCoords.x * 40, foodCoords.y * 40 + 60, 40, 40), 0)
        for i in range(1, len(snake), 1):
            pygame.draw.rect(screen, "yellow", (snake[i].x * 40, snake[i].y * 40 + 60, 40, 40), 0)
        pygame.draw.rect(screen, "red", (snake[0].x * 40, snake[0].y * 40 + 60, 40, 40), 0)
        if not alive:
            game_music.stop()
            pygame.draw.rect(screen, "white", (0, 290, 1200, 200), 0)
            death_text = death_font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(death_text, (300, 350))
            # Game Over anzeigen, weiss, roter hintergrund...

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
