import pygame, sys, time, random
from pygame.locals import *

# configurar pygame
pygame.init()
relojPrincipal = pygame.time.Clock()

# configurar la ventana
ANCHOVENTANA = 400
ALTOVENTANA = 400

superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)
pygame.display.set_caption('Sprite y Sonido')

# configurar los colores
NEGRO = (0, 0, 0)

# configurar la estructura de bloque de datos
jugador = pygame.Rect(300, 100, 40, 40)
imagenJugador = pygame.image.load('jugador.png')
imagenEstidadaJugador = pygame.transform.scale(imagenJugador, (40, 40))
imagenComida = pygame.image.load('cereza.png')
comidas = []
for i in range(20):
    comidas.append(pygame.rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ANCHOVENTANA - 20), 20, 20))

    contadorComida = 0
    NUEVACOMIDA = 40

    # configurar variables del teclado
    moverseIzquierda = False
    moverseDerecha = False
    moverseArriba = False
    moverseAbajo = False

    VELOCIDADMOVIMIENTO = 6

    # configurar musica
    sonidoRecoleccion = pygame.mixer.Sound('recoleccion.wav')
    pygame.mixer.music.load('musicaDeFondo.mid')
    pygame.mixer.music.play(-1, 0.0)
    musicaSonando = True

    # ejecutar el bucle del juego
    while True:
        # comprobar si se ha disparado el evento QUIT (salir)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                # cambiar las variables del teclado
                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverseDerecha = False
                    moverseIzquier = True
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverseIzquierda = False
                    moverseDerecha = True
                if evento.key == K_UP or evento.key == ord('w'):
                    moverseAbajo = False
                    moverseArriba = True
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverseArriba = False
                    moverseAbajo = True
            if evento.type == KEYUP:
                if evento.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverseIzquierda = False
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverseDerecha = False
                if evento.key == K_UP or evento.key == ord('w'):
                    moverseArriba = False
                if evento.key == K_DOWN or evento.key == ord('S'):
                    moverseAbajo = False
                if evento.key == ord('x'):
                    jugador.top = random.randint(0, ALTOVENTANA - jugador.height)
                    jugador.left = random.randint(0, ANCHOVENTANA - jugador.width)