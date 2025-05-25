import pygame
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
    def __init__(self, x, y, color, typ, direction):
        self.x = x
        self.y = y
        self.color = color
        self.typ = typ
        self.direction = direction

playerDirection = Direction.RIGHT

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

    gameField = [
        [GameFieldObject(x, y, "black", GameFieldObjectType.EMPTY, Direction.NONE) for x in range(30)]
        for y in range(24)
    ]
    gameField[10][10] = GameFieldObject(10, 15, "red", GameFieldObjectType.HEAD, Direction.RIGHT)
    gameField[9][10] = GameFieldObject(10, 15, "yellow", GameFieldObjectType.SNAKE, Direction.RIGHT)
    gameField[8][10] = GameFieldObject(10, 15, "yellow", GameFieldObjectType.SNAKE, Direction.RIGHT)

    clock = pygame.time.Clock()
    running = True

    logic_timer = 0
    logic_interval = 1.0  # 1x pro Sekunde

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
                obj = gameField[x][y]
                if obj.typ != GameFieldObjectType.EMPTY:
                    pygame.draw.rect(screen, obj.color, (x * 40, y * 40 + 60, 40, 40), 0)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
