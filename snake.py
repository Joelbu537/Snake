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

class FoodCoordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

playerDirection = Direction.RIGHT
gameField = [
    [GameFieldObject(x, y, GameFieldObjectType.EMPTY, Direction.NONE) for x in range(30)]
    for y in range(24)
]
gameField[10][10] = GameFieldObject(10, 15, GameFieldObjectType.HEAD, Direction.RIGHT)
gameField[9][10] = GameFieldObject(10, 15, GameFieldObjectType.SNAKE, Direction.RIGHT)
gameField[8][10] = GameFieldObject(10, 15, GameFieldObjectType.SNAKE, Direction.RIGHT)

def new_food():
    is_valid = False
    while not is_valid:
        temp_coords = FoodCoordinates(random.randint(0, 29), random.randint(0, 23))
        if gameField[temp_coords.x][temp_coords.y].typ ==  GameFieldObjectType.EMPTY:
            print("Food set to " + str(temp_coords.x) + " " + str(temp_coords.y))
            gameField[temp_coords.x][temp_coords.y].typ = GameFieldObjectType.FOOD
            return temp_coords

foodCoords = new_food()

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

def update_game_logic(gameField):
    #  LOGIK HINZUFÜGEN!!!

    print(f"Direction: {playerDirection}")

def main():
    global playerDirection
    pygame.init()
    screen = pygame.display.set_mode((1200, 780))
    pygame.display.set_caption("Snake")
    pygame.mouse.set_visible(True)

    clock = pygame.time.Clock()
    running = True

    logic_timer = 0
    logic_interval = 1.0  # Updates/Sekunde, vielleicht 90° Parabel oder so?

    while running:
        dt = clock.tick(60) / 1000  # 60 FPS
        logic_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input()  # Läuft mit 60 FPS

        if logic_timer >= logic_interval:
            update_game_logic(gameField)
            logic_timer = 0  # Reset Timer

        # Fenster füllen
        screen.fill("black")
        pygame.draw.rect(screen, "cyan", (0, 0, 1200, 60), 0)
        for x in range(len(gameField)):
            for y in range(len(gameField[0])):
                field = gameField[x][y]
                if field.typ == GameFieldObjectType.SNAKE:
                    pygame.draw.rect(screen, "yellow", (x * 40, y * 40 + 60, 40, 40), 0)
                elif field.typ == GameFieldObjectType.HEAD:
                    pygame.draw.rect(screen, "red", (x * 40, y * 40 + 60, 40, 40), 0)
                elif field.typ == GameFieldObjectType.FOOD:
                    pygame.draw.rect(screen, "green", (x * 40, y * 40 + 60, 40, 40), 0)

        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()
