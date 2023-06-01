import pygame

pygame.init()

screen = pygame.display.set_mode([500,500])
correr_juego = True

while correr_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr_juego = False
    
    screen.fill((250,0,0))
    pygame.draw.circle(screen,(255,255,0),(250,250),75)
    pygame.display.flip()
    
pygame.quit()