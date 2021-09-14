
import pygame
def left_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return True
    return False

def right_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        return True
    return False

def up_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        return True
    return False

def down_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        return True
    return False

def plus_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_PLUS]:
        return True
    return False

def minus_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_MINUS]:
        return True
    return False

def equals_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_EQUALS]:
        return True
    return False

def enter_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return True
    return False

"""
import pygame

running = True
verde_escuro = (0,128,0)

# Inicializa pygame
pygame.init();

# Inicializa janela com fundo verde escuro
screen = pygame.display.set_mode((1350, 480))
screen.fill(verde_escuro)

# Carrega uma imagem PNG com transparencia
img = pygame.image.load("piso_piso.png").convert_alpha()

# Recupera as dimensoes da imagem
w, h = img.get_size()
print(img.get_size())
# Escalas da imagem
scales = [ 1, 0.88, 0.75, 0.5, 0.33, 0.25, 0.1 ]

# Exibe a mesma imagem, em escalas diferentes, lado a lado.
posx = 0
for s in scales:
    redim = pygame.transform.smoothscale( img, (int(w*s), int(h*s)) )
    screen.blit( redim, (posx, 0) )
    posx += int(w*s)

# Loop principal de eventos
clock = pygame.time.Clock()
while running:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# Fim
pygame.exit()
sys.exit()
"""
