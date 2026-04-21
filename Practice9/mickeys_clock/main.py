import pygame 
from datetime import datetime

pygame.init()
width = 500
heigth = 500
screen = pygame.display.set_mode((width, heigth))
done = False
clock = pygame.time.Clock()

image = pygame.image.load("images/mickeyclock.jpg")
image = pygame.transform.scale(image, (width, heigth))
sec0 = pygame.image.load("images\hand1.png")
min0 = pygame.image.load("images\hand1.png")


center = (width//2, heigth//2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.now()
    seconds = now.second
    minutes = now.minute

    sec_angle = -seconds * 6
    min_angle = -minutes * 6

    sec_rot = pygame.transform.rotate(sec0, sec_angle)
    min_rot = pygame.transform.rotate(min0, min_angle)
    
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))

    screen.blit(sec_rot, sec_rot.get_rect(center=center))
    screen.blit(min_rot, min_rot.get_rect(center=center))

    pygame.display.flip()
    clock.tick(60)    