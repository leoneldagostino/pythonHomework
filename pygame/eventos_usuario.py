import pygame





#para poder fijar un evento que ocupa por tiempo
pygame.init()

tick = pygame.USEREVENT + 0 #mete  evento en cola
screen = pygame.display.set_mode([500,500])#seteamos la pantalla 
pygame.time.set_timer(tick,1000)#seteamos el tiempo que va ejecutar un evento

correr_juego = True

while correr_juego:
    for evento in pygame.event.get():
        if evento.type == tick:
            print("Ya paso un segundo")
            
        if evento.type == pygame.QUIT :#cuando cierra la ventana se termina el juego
            correr_juego = False
            
    screen.fill((250,0,0))#pinta el fondo de la pantalla
    pygame.draw.circle(screen,(255,255,0),(0,25),105)#dibuja un circulo (en pantalla,damos color, ubicamos el circulo, damos el radio)
    pygame.display.flip()            
            
pygame.quit()