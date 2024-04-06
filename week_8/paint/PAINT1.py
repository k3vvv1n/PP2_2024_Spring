import pygame
import pygame.gfxdraw

screen = pygame.display.set_mode((700, 500))
another_layer = pygame.Surface((700, 500))
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))
png = pygame.image.load("images/sss.jpg")

pygame.init()

white = (255, 255, 255)
blue = (67, 238, 250)
red = (255, 0, 0)
black = (0, 0, 0)
green = (38, 245, 45)
pink = (255, 192, 203)
orange = (255, 165, 0)
yellow = (255, 255, 0)

color = black


done = False
clock = pygame.time.Clock()

x1 = 10
y1 = 10
x2 = 10
y2 = 10


col1 = (22, 81, 30, 34)
col2 = (56, 81, 34, 34)
col3 = (22, 120, 30, 33)
col4 = (56, 120, 34, 32)
col5 = (22, 156, 30, 33)
col6 = (56, 156, 34, 32)
col7 = (22, 192, 30, 33)
Eraser = (56, 192, 34, 32)
buttonselect = (22, 81, 30, 34)


def drawrectangle():
    pygame.gfxdraw.box(screen, col1, black)
    pygame.gfxdraw.box(screen, col2, blue)
    pygame.gfxdraw.box(screen, col3, red)
    pygame.gfxdraw.box(screen, col4, green)
    pygame.gfxdraw.box(screen, col5, pink)
    pygame.gfxdraw.box(screen, col6, orange)
    pygame.gfxdraw.box(screen, col7, yellow)
    pygame.gfxdraw.box(screen, Eraser, white)


drawrectangle()

pygame.mouse.set_cursor(*pygame.cursors.broken_x)

mousepos = pygame.mouse.get_pos()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        t = pygame.mouse.get_pressed()
        if t[0] == 1:
            mousepos = pygame.mouse.get_pos()
            if 122 < mousepos[0] < 678 and 21 < mousepos[1] < 480:
                pygame.gfxdraw.filled_ellipse(
                    screen, mousepos[0], mousepos[1], 8, 8, color
                )

        elif 22 < mousepos[0] < 52 and 81 < mousepos[1] < 115:
            color = black
            drawrectangle()
            buttonselect = (22, 81, 30, 34)

        elif 56 < mousepos[0] < 90 and 81 < mousepos[1] < 115:
            color = blue
            drawrectangle()
            buttonselect = (56, 81, 34, 34)

        elif 22 < mousepos[0] < 52 and 120 < mousepos[1] < 153:
            color = red
            drawrectangle()
            buttonselect = (22, 120, 30, 33)

        elif 56 < mousepos[0] < 90 and 120 < mousepos[1] < 152:
            color = green
            drawrectangle()
            buttonselect = (56, 120, 34, 32)

        elif 22 < mousepos[0] < 52 and 156 < mousepos[1] < 189:
            color = pink
            drawrectangle()
            buttonselect = (22, 156, 30, 33)

        elif 56 < mousepos[0] < 90 and 156 < mousepos[1] < 188:
            color = orange
            drawrectangle()
            buttonselect = (56, 156, 34, 32)

        elif 22 < mousepos[0] < 52 and 192 < mousepos[1] < 225:
            
            drawrectangle()
            buttonselect = (22, 192, 30, 33)
        # Eraser
        elif 56 < mousepos[0] < 90 and 192 < mousepos[1] < 224:
            color = white
            drawrectangle()
            buttonselect = (56, 192, 34, 32)

    screen.blit(png, (56, 192,34, 32))
    pygame.display.flip()
    clock.tick(60)
