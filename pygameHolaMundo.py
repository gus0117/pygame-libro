import pygame, sys
from pygame.locals import *

#configurar pygame
pygame.init()

# configurar la ventana
superficieVentana = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hola Mundo!')

#Configurar los colors
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Configurar fuentes
fuenteBasica = pygame.font.SysFont(None, 48)

#Configurar el texto
texto = fuenteBasica.render('Hola mundo', True, BLANCO, AZUL)
textRect = texto.get_rect()
textRect.centerx = superficieVentana.get_rect().centerx
textRect.centery = superficieVentana.get_rect().centery

#pintar un fondo blanco sobre la ventana
superficieVentana.fill(BLANCO)

#dibujar un poligono verde sobre la superficie
pygame.draw.polygon(superficieVentana, VERDE, ((146, 0), (291, 106,), (236, 277), (56, 277), (0, 106)))

#dibujar algunas lineas azules sobre la superficie
pygame.draw.line(superficieVentana, AZUL, (60, 60), (120, 60), 4)
pygame.draw.line(superficieVentana, AZUL, (120,60), (60, 120))
pygame.draw.line(superficieVentana, AZUL, (60, 120), (120, 120), 4)

#dibujar un circulo azul sobre la superficie
pygame.draw.circle(superficieVentana, AZUL, (300, 50), 20, 0)

#dibujar una elipse roja sobre la superficie
pygame.draw.ellipse(superficieVentana, ROJO, (300, 250, 40, 80), 1)

#dibujar el rectanglo de fondo para el texto sobre la superficie
pygame.draw.rect(superficieVentana, ROJO, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

#obtener un arreglo de pixeles de la superficie
arregloDePixeles = pygame.PixelArray(superficieVentana)
arregloDePixeles[480][380] = NEGRO
del arregloDePixeles

#dibujar el texto sobre la superficie
superficieVentana.blit(texto, textRect)

#dibujar la ventana sobre la pantalla
pygame.display.update()

#ejectuar el bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

