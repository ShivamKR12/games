import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Ball properties
BALL_RADIUS = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = -5

# Platform properties
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20

# Cube properties
CUBE_SIZE = 40

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 50
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with walls
        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y <= 0:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), BALL_RADIUS)

class Platform:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2
        self.y = SCREEN_HEIGHT - PLATFORM_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    def check_collision(self, ball):
        # Check collision between ball and platform
        if (self.y <= ball.y + BALL_RADIUS <= self.y + PLATFORM_HEIGHT and
            self.x <= ball.x <= self.x + PLATFORM_WIDTH):
            ball.speed_y *= -1

class Cube:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.destroyed = False

    def draw(self):
        if not self.destroyed:
            pygame.draw.rect(screen, WHITE, (self.x, self.y, CUBE_SIZE, CUBE_SIZE))

def main():
    ball = Ball()
    platform = Platform()

    cubes = []
    for i in range(10):
        for j in range(5):
            cubes.append(Cube(i * (CUBE_SIZE + 10), j * (CUBE_SIZE + 10)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and platform.x > 0:
            platform.x -= 5
        if keys[pygame.K_RIGHT] and platform.x < SCREEN_WIDTH - PLATFORM_WIDTH:
            platform.x += 5

        screen.fill((0, 0, 0))

        ball.update()
        ball.draw()

        platform.draw()
        platform.check_collision(ball)

        for cube in cubes:
            cube.draw()
            if not cube.destroyed:
                if (ball.x - BALL_RADIUS < cube.x + CUBE_SIZE and
                    ball.x + BALL_RADIUS > cube.x and
                    ball.y - BALL_RADIUS < cube.y + CUBE_SIZE and
                    ball.y + BALL_RADIUS > cube.y):
                    cube.destroyed = True
                    ball.speed_y *= -1

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
