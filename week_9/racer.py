#images you can see in week_8

import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 600))

FPS = pygame.time.Clock()
FPS.tick(60)

score=0
SPEED = 5

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF.fill(WHITE)

pygame.display.set_caption("Racer")
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("racer/back.png")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/coin.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 560), 0)
        self.weight = (random.randint(1,5))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/truck.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 560), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def inc_speed(self):
        self.speed += 3

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/Audi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.score = 0

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right > 0:
            if pressed[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()
C1 = Coin()
Enemies = pygame.sprite.Group()
Enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

coins = pygame.sprite.Group()
coins.add(C1)

capacity =0
"""inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)"""

while True:
    for event in pygame.event.get():
        """if event.type == inc_speed:
            SPEED += 0.5
"""
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()
    C1.move()

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(score), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)

    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collided_coins:
        score += coin.weight
        capacity += coin.weight
        coins.remove(coin)  # Удаляем столкнувшуюся монету
        C1 = Coin()  # Создаем новую монету
        coins.add(C1)
    
    if capacity>=10:
        capacity -= 10
        SPEED += 5

    your_score = font_small.render(f"Youre score is {score}", True, BLACK)
    if pygame.sprite.spritecollideany(P1, Enemies):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        DISPLAYSURF.blit(your_score, (30, 320))

        pygame.display.update()
        for cars in all_sprites:
            cars.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FPS.tick(60)
