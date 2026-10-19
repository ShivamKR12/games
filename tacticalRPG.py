import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player and Enemy Classes
class Entity:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

class Player(Entity):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

class Enemy(Entity):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

# Game initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turn-Based Tactical RPG")
clock = pygame.time.Clock()

# Map initialization
MAP = [
    "##########",
    "#........#",
    "#.###..###",
    "#...E..#.#",
    "#...###..#",
    "#........#",
    "#####P####"
]

def draw_map(surface):
    for y, row in enumerate(MAP):
        for x, tile in enumerate(row):
            if tile == "#":
                pygame.draw.rect(surface, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile == "P":
                pygame.draw.rect(surface, BLUE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile == "E":
                pygame.draw.rect(surface, RED, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Game loop
def main():
    player = Player(7, 6, BLUE)
    enemies = [Enemy(4, 3, RED)]

    while True:
        screen.fill(WHITE)
        draw_map(screen)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Player movement
                if event.key == pygame.K_UP:
                    if MAP[player.y - 1][player.x] != "#":
                        player.y -= 1
                elif event.key == pygame.K_DOWN:
                    if MAP[player.y + 1][player.x] != "#":
                        player.y += 1
                elif event.key == pygame.K_LEFT:
                    if MAP[player.y][player.x - 1] != "#":
                        player.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if MAP[player.y][player.x + 1] != "#":
                        player.x += 1

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
