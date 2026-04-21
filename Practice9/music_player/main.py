import pygame 

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 400))
done = False

playlist = ['music\_track1.wav', 'music\_track2.wav']
index = 0

font = pygame.font.SysFont("ST Rome", 36)

status = "Stopped"

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)
                status = "Playing"

            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                status = "Stopped" 

            if event.key == pygame.K_n:
                pygame.mixer.music.stop()
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                status = "Next"

            if event.key == pygame.K_b:
                pygame.mixer.music.stop()
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
                status = "Back"
                
            if event.key == pygame.K_q:
                done = True
    
    screen.fill((255, 255, 255))

    text = font.render(playlist[index], True, (0, 0, 0))
    screen.blit(text, (250 - text.get_width() // 2, 200 - text.get_height() // 2))

    time = pygame.mixer.music.get_pos() // 1000
    text_time = font.render(f"Time: {time}", True, (0, 0, 0))
    screen.blit(text_time, (10, 10))

    status_text = font.render(f"Status: {status}", True, (0, 0, 0))
    screen.blit(status_text, (10, 40))

    pygame.display.flip()
