import pygame, sys, random
from pygame.locals import *

def verifSuperpositionRects(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Verifica si las esquinas de a se encuentran dentro de b
        if ((puntoDentroDeRect(a.left, a.top, b)) or
            (puntoDentroDeRect(a.left, a.bottom, b)) or
            (puntoDentroDeRect(a.right, a.top, b)) or
            (puntoDentroDeRect(a.right, a.bottom, b))):
            return True
    return False

def puntoDentroDeRect(x, y, rect):
    if(x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False


# establece el juego
pygame.init()
relojPrincipal = pygame.time.Clock()

# establece la ventana
ANCHOVENTANA = 400
ALTOVENTANA = 400
superficeVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)

# establece las variables de direccion
ABAJOIZQUIERDA = 1
ABAJODERECHA = 3
ARRIBAIZQUIERDA = 7
ARRIBADERECHA = 9

VELOCIDADMOVIMIENTO = 4

# establece los colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

#establece las estructuras de datos de comida y rebotin
contadorComida = 0
NUEVACOMIDA = 40
TAMANIOCOMIDA = 20
rebotin = {'rect': pygame.Rect(300, 100, 50, 50), 'dir': ARRIBAIZQUIERDA}
comidas = []
for i in range(20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMANIOCOMIDA), random.randint(0, ALTOVENTANA - TAMANIOCOMIDA), TAMANIOCOMIDA, TAMANIOCOMIDA))

# corre el bucle de juego
while True:
    # busca un evento QUIT
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    contadorComida += 1
    if contadorComida >= NUEVACOMIDA:
        #add nueva comida
        contadorComida = 0
        comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMANIOCOMIDA), random.randint(0, ALTOVENTANA - TAMANIOCOMIDA), TAMANIOCOMIDA, TAMANIOCOMIDA))

    #Dibuja el fondo NEGRO osbre la superficie
    superficeVentana.fill(NEGRO)

    # Mueve la estructura de datos rebotin
    if rebotin['dir'] == ABAJOIZQUIERDA:
        rebotin['rect'].left -= VELOCIDADMOVIMIENTO
        rebotin['rect'].top += VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ABAJODERECHA:
        rebotin['rect'].left += VELOCIDADMOVIMIENTO
        rebotin['rect'].top += VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ARRIBAIZQUIERDA:
        rebotin['rect'].left -= VELOCIDADMOVIMIENTO
        rebotin['rect'].top -= VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ARRIBADERECHA:
        rebotin['rect'].left += VELOCIDADMOVIMIENTO
        rebotin['rect'].top -= VELOCIDADMOVIMIENTO

    # Verifica si rebotin se movio fuera de la ventana
    if rebotin['rect'].top < 0:
        # rebotin se movio por arriba de la ventana
        if rebotin['dir'] == ARRIBAIZQUIERDA:
            rebotin['dir'] = ABAJOIZQUIERDA
        if rebotin['dir'] == ARRIBADERECHA:
            rebotin['dir'] = ABAJODERECHA
    if rebotin['rect'].bottom > ALTOVENTANA:
        # rebotin se movio por debajo de la ventana
        if rebotin['dir'] == ABAJOIZQUIERDA:
            rebotin['dir'] = ARRIBAIZQUIERDA
        if rebotin['dir'] == ABAJODERECHA:
            rebotin['dir'] = ARRIBADERECHA
    if rebotin['rect'].left < 0:
        # rebotin se movio por la izquierda de la ventana
        if rebotin['dir'] == ABAJOIZQUIERDA:
            rebotin['dir'] = ABAJODERECHA
        if rebotin['dir'] == ARRIBAIZQUIERDA:
            rebotin['dir'] = ARRIBADERECHA
    if rebotin['rect'].right > ANCHOVENTANA:
        # rebotin se movio por la derecha de la ventana
        if rebotin['dir'] == ABAJODERECHA:
            rebotin['dir'] = ABAJOIZQUIERDA
        if rebotin['dir'] == ARRIBADERECHA:
            rebotin['dir'] = ARRIBAIZQUIERDA
    
    # Dibuja a rebotin en la superficie
    pygame.draw.rect(superficeVentana, BLANCO, rebotin['rect'])

    # Verificia si rebotin intersecto algun cuadrado de comida
    for comida in comidas[:]:
        if verifSuperpositionRects(rebotin['rect'], comida):
            comidas.remove(comida)

    # Dibuja la comida
    for i in range(len(comidas)):
        pygame.draw.rect(superficeVentana, VERDE, comidas[i])
    
    # Dibuja la ventana en la pantalla
    pygame.display.update()
    relojPrincipal.tick(40)
       
       


