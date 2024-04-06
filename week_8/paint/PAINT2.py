import pygame

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)
    
def getCircle(x1, y1, x2, y2):
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    radius = max(abs(x1 - x2), abs(y1 - y2)) // 2
    return (x, y, radius)


WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
another_layer = pygame.Surface((WIDTH, HEIGHT))

done = False
clock = pygame.time.Clock()

x1 = 10
y1 = 10
x2 = 10
y2 = 10


leftClick = False
rightClick = False
isMouseDown = False
color = (0, 128, 255)
isMouseDown = False
screen.fill((0, 0, 0))

while not done:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        '''draw rect and circle with mouse'''
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x1 = event.pos[0]
            y1 = event.pos[1]
            isMouseDown = True

            if event.button == 1: # left click
                leftClick = True
            if event.button == 3: # right click
                rightClick = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            isMouseDown = False
            another_layer.blit(screen, (0, 0))
            
            if event.button == 1:
                leftClick = False    
            if event.button == 3:
                rightClick = False
            
        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                x2 = event.pos[0]
                y2 = event.pos[1]
                screen.blit(another_layer, (0, 0))
                if leftClick:
                    pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                if rightClick:
                    pygame.draw.circle(screen, color, getCircle(x1, y1, x2, y2)[:2], getCircle(x1, y1, x2, y2)[2], 1)

    pygame.display.flip()
    clock.tick(60)