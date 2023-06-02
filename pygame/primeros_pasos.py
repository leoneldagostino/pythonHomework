import pygame

pygame.init()

screen = pygame.display.set_mode([500,500])#seteamos la pantalla 
correr_juego = True

while correr_juego:
    for evento in pygame.event.get():#verificamos la cola de eventos
        if evento.type == pygame.QUIT :#cuando cierra la ventana se termina el juego
            correr_juego = False
    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_x:#se verifica que toca la tecla (x en este caso)
                print("Se presiono la tecla x")#al apretarse informamos en consola  
            if evento.key == pygame.K_z:
                correr_juego = False
    screen.fill((250,0,0))#pinta el fondo de la pantalla
    pygame.draw.circle(screen,(255,255,0),(0,25),5)#dibuja un circulo (en pantalla,damos color, ubicamos el circulo, damos el radio)
    pygame.display.flip()# traemos los cambios realizados en pantalla
    
pygame.quit()