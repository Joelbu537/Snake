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
gameField = [
    [
        GameFieldObject(x, y, "black", GameFieldObjectType.EMPTY, Direction.NONE)
        for x in range(30)
    ]
    for y in range(24)
]
playerDirection = Direction.NONE
gameField[10][10] = GameFieldObject(10, 15, "red", GameFieldObjectType.HEAD, Direction.RIGHT)
gameField[9][10] = GameFieldObject(10, 15, "yellow", GameFieldObjectType.SNAKE, Direction.RIGHT)
gameField[8][10] = GameFieldObject(10, 15, "yellow", GameFieldObjectType.SNAKE, Direction.RIGHT)

pygame.init()
info = pygame.display.Info()

screen = pygame.display.set_mode((1200, 780))#, pygame.SCALED)
pygame.display.set_caption("Snake")
pygame.mouse.set_visible(True)

clock = pygame.time.Clock()
running = True
dt = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.draw.rect(screen, "cyan", (0, 0, info.current_w, 60), 0)

    for x in range(len(gameField)):
        for y in range(len(gameField[0])):
            if gameField[x][y] == 1:
                pass
    for x in range(len(gameField)):
        for y in range(len(gameField[0])):
            if gameField[x][y].typ == GameFieldObjectType.EMPTY:
                pygame.draw.rect(screen, "black", (x * 40, y * 40 + 60, 40, 40), 0)
            if gameField[x][y].typ == GameFieldObjectType.HEAD:
                pygame.draw.rect(screen, gameField[x][y].color, (x * 40, y * 40 + 60, 40, 40), 0)
            if gameField[x][y].typ == GameFieldObjectType.SNAKE:
                pygame.draw.rect(screen, gameField[x][y].color, (x * 40, y * 40 + 60, 40, 40), 0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_w]:
        playerDirection = Direction.UP
    if keys[pygame.K_s]:
        playerDirection = Direction.DOWN
    if keys[pygame.K_a]:
        playerDirection = Direction.LEFT
    if keys[pygame.K_d]:
        playerDirection = Direction.RIGHT

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(1) / 1000

pygame.quit()