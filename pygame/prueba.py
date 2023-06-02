import pygame
import random
pygame.init()
correr_juego = True

screen = pygame.display.set_mode([500,500])#seteamos la pantalla 
imagen = pygame.image.load("pygame\pelota.png")
rect_imagen = imagen.get_rect()
rect_imagen.centerx = 150
rect_imagen.centery = 200

tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick,75)

letra_presionada = pygame.key.get_pressed()

while correr_juego:
    screen.fill((0,0,0))
    for evento in pygame.event.get():#verificamos la cola de eventos
        if evento.type == pygame.QUIT :#cuando cierra la ventana se termina el juego
            correr_juego = False   
        if evento.type == tick:
            
            
            movimiento_x = random.randint(-100,100)
            movimiento_y = random.randint(-100,100)

            rect_imagen.centerx += movimiento_x
            rect_imagen.centery += movimiento_y
            
            rect_imagen.x = max(0,min(rect_imagen.x,500 - rect_imagen.width))
            rect_imagen.y = max(0,min(rect_imagen.y,500 - rect_imagen.height))

        

    screen.blit(imagen,rect_imagen)
    pygame.display.flip() 
    
    
pygame.quit()



