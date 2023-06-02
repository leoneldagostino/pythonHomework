import pygame

pygame.init()

screen = pygame.display.set_mode([500,500])#seteamos la pantalla 
correr_juego = True

fuente = pygame.font.SysFont("Arial Narrow",50)#tipo de fuente, tamaño
texto = fuente.render("Hola mundo",True,(0,250,0))#damos lo que queremos lo que escribira y el color
print(type(texto))#clase surface



while correr_juego:
    for evento in pygame.event.get():#verificamos la cola de eventos
        if evento.type == pygame.QUIT :#cuando cierra la ventana se termina el juego
            correr_juego = False
            


    screen.blit(texto,(250,250))#lo llevamos a la screen
    screen.fill((250,0,0))#pinta el fondo de la pantalla
    pygame.draw.circle(screen,(255,255,0),(0,25),5)#dibuja un circulo (en pantalla,damos color, ubicamos el circulo, damos el radio)
    pygame.display.flip()# traemos los cambios realizados en pantalla
    
pygame.quit()