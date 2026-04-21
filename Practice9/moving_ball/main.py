import pygame 

pygame.init()
width = 800
heigth = 700
screen = pygame.display.set_mode((width, heigth))
done = False

clock = pygame.time.Clock()
color = (225, 0, 0)
x, y = width//2, heigth//2
rad = 25
pic = 20

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x - pic - rad >= 0:
                    x -= pic
            if event.key == pygame.K_RIGHT:
                if x + pic + rad <= width:
                    x += pic
            if event.key == pygame.K_UP:
                if y - pic - rad >= 0:
                    y -= pic
            if event.key == pygame.K_DOWN:
                if y + pic + rad <= heigth:
                    y += pic

    screen.fill((225, 225, 225))
    pygame.draw.circle(screen, color, (x, y), rad)
    
    pygame.display.flip()
