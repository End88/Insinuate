# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import pygame
import math
from arrow import up_is_down, down_is_down, left_is_down, right_is_down


def enter_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return True
    return False
# from random import randint


def txt(message, position_txt_x, position_txt_y, color=(255, 255, 255), size_txt=30, font="david"):
    font = pygame.font.SysFont(font, size_txt)
    text = font.render(message, True, color)

    center = []
    for i in text.get_rect():
        center.append(i)
    s.blit(text, [position_txt_x - center[2] / 2, position_txt_y - center[3] / 2])


def dist(pont1_x, pont1_y, pont2_x, pont2_y):
    return math.sqrt(math.pow(pont1_x - pont2_x, 2) + math.pow(pont1_y - pont2_y, 2))


def collision(rect, circle):
    if rect.x <= circle.x <= rect.x + rect.width:
        if circle.y + circle.rad >= rect.y and circle.y - circle.rad <= rect.y + rect.height:
            return True

    if circle.y + circle.rad >= rect.y and circle.y - circle.rad <= rect.y + rect.height:
        if circle.x + circle.rad >= rect.x and circle.x - circle.rad <= rect.x + rect.width:
            if circle.x + circle.rad - rect.x <= 10:
                return True

    if dist(circle.x, circle.y, rect.x, rect.y) <= circle.rad or \
            dist(circle.x + rect.width, circle.y, rect.x, rect.y) <= circle.rad or \
            dist(circle.x, circle.y + rect.height, rect.x, rect.y) <= circle.rad or \
            dist(circle.x + rect.width, circle.y + rect.height, rect.x, rect.y) <= circle.rad:
        return True
    return False


def ball_collision(ball1, ball2):
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y

    distance = math.sqrt(dx * dx + dy * dy)
    if distance < ball1.rad + ball2.rad:
        return True
    else:
        return False


list_enemies = [[], [], [], [], []]


def create_ball(x, y, group):
    enemies = Obstacles(x, y, 5)
    list_enemies[group].append(enemies)  # noinspection PyTypeChecker


now = datetime.datetime.now()


def restart_now():
    global now
    now = datetime.datetime.now()


class Obstacles:
    def __init__(self, x, y, rad, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.ini_x = x
        self.ini_y = y
        self.rad = rad
        self.color = color
        self.accelerator = 0
        self.speed = 10
        n = pygame.time.get_ticks()
        self.second_created = n

    def draw_obstacle(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad)


class Walls:
    def __init__(self, x, y, swidth, sheight, angle=0, color=(102, 102, 102)):
        self.x = x
        self.y = y
        self.width = swidth
        self.height = sheight
        self.angle = angle
        self.color = color

    def draw_wall(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Persona:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad


def phase_one_part_one():
    black = (0, 0, 0)
    white = (255, 255, 255)
    bg1 = pygame.image.load('data\\images\\bg1.png')
    bg2 = pygame.image.load('data\\images\\bg2.png')
    bg3 = pygame.image.load('data\\images\\bg3.png')

    psg = Persona(width / 2, height / 2, 10)
    wall_1 = Walls(0, 0, 750, 25, 0)
    wall_2 = Walls(0, 480 - 25, 750, 25, 0)
    wall_3 = Walls(0, 0, 25, 480, 0)
    wall_4 = Walls(750, 0, 750+275, 25, 0)
    wall_5 = Walls(750, 480 - 25, 750 + 275, 25, 0)
    wall_6 = Walls(1500, -480, 25, 480 + 25, 0)
    wall_7 = Walls(1500, 480 - 25, 25, 480, 0)
    wall_8 = Walls(2250 - 25, 0, 25, 480, 0)
    wall_15 = Walls(500, 0, 200, height / 2 - 20, 0)
    wall_16 = Walls(500, height / 2 + 20, 200, height / 2 - 20, 0)
    wall_17 = Walls(500, height / 2 - 20, 10, 40, 0)
    list_walls = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_15, wall_16, wall_17]

    way_one = Walls(1775, 0, 750-275, 25, 0, (102, 102, 162))
    way_two = Walls(1775, 480-25, 750-275, 25, 0, (162, 102, 102))
    list_end_phase = [way_one, way_two]

    copy_walls = []
    for i in list_walls:
        copy_wall = Walls(i.x, i.y, i.width, i.height, i.angle)
        copy_walls.append(copy_wall)

    copy_ways = []
    for i in list_end_phase:
        copy_way = Walls(i.x, i.y, i.width, i.height, i.angle)
        copy_ways.append(copy_way)

    list_txt = [["Olá", 50, 2], ["É bom te ver.", 30, 3], ["Fico feliz que esteja aqui", 50, 4], ["Talvez...", 90, 1],
                ["eu possa te ensinar algumas coisas", 20, 5], ["Okay. primeiro;", 50, 2],
                ["as setas são nossas direções", 25, 5], ["tente pressionar aquele botão", 25, 5], ["Segundo", 90, 2],
                ["tome cuidado com as paredes", 25, 5],
                ["Agora vê aquilo?", 60, 4], ["não se deixe acertar por elas", 30, 5], ["maravilhoso!", 90, 2],
                ["Está pronto para seguir", 50, 3], ["Vá em frente", 60, 2], ["Espere um pouco", 25, 2],
                ["Escolhas...", 25, 6], ["Teremos tantas durante a vida.", 75, 6],
                ["Algumas simples, como esta", 50, 4], ["Para cima há flores", 30, 3], ["para baixo, espinhos", 30, 3],
                ["mantenha-se seguro", 75, 4], ["suba", 90, 10]]

    clock = pygame.time.Clock()
    for i in range(5):
        create_ball(900, i * 50, 0)

    button = Obstacles(490, 50, 8, (0, 128, 255))

    fade = 0
    next_txt = 0
    velocity = 5
    move_x = 0
    move_y = 0
    close = False
    while not close:
        # _______________________________________________ Desenhos na tela
        screen.fill(black)  # Limpa tela
        s.fill((0, 0, 0, 0))  # Limpa a tela da surface S (responsável pelo texto)
        s.set_alpha(fade)  # Define a transparência novamente
        screen.blit(bg1, (0 + move_x, 0 + move_y))  # Background 1 até 3
        screen.blit(bg2, (750 + move_x, 0 + move_y))
        screen.blit(bg3, (1500 + move_x, 0 + move_y))
        way_one.draw_wall()
        way_two.draw_wall()
        for n in list_enemies[0]:
            n.draw_obstacle()  # Desenho de todos os inimigos
        for i in list_walls:
            i.draw_wall()  # Desenho de todas as paredes
        button.draw_obstacle()
        txt(list_txt[next_txt][0], width / 2, height / 2 + 100, white, 45, "imprintshadow")
        screen.blit(s, (0, 0))
        pygame.draw.circle(screen, (255, 255, 255), (psg.x, psg.y), psg.rad)  # Desenho do personagem

        # _________________________________________________________________________ txt appear and desappear
        fade_velocity = list_txt[next_txt][1]
        if 255 >= fade >= 0:
            fade += fade_velocity

        dif = datetime.datetime.now() - now
        if dif.seconds >= list_txt[next_txt][2]:
            if fade > 255:
                if not (wall_17 in list_walls) or next_txt < 7:  # Primeira trava de texto
                    if -move_x > 345 or next_txt < 9:
                        if -move_x > 730 or next_txt < 11:
                            if -move_x > 1400 or next_txt < 14:
                                fade = 255
                                list_txt[next_txt][1] = -list_txt[next_txt][1]
            if fade < 0:
                fade = 0
                restart_now()
                if next_txt < len(list_txt)-1:
                    next_txt += 1
        # _________________________________________________________________________ enemies 1
        # movimentação dos primeiros inimigos
        for i in range(len(list_enemies[0])):
            list_enemies[0][i].accelerator += list_enemies[0][i].speed
            list_enemies[0][i].x = list_enemies[0][i].ini_x + move_x
            list_enemies[0][i].y = list_enemies[0][i].ini_y + move_y + list_enemies[0][i].accelerator
            if list_enemies[0][i].y >= height + move_y or list_enemies[0][i].y <= 0 + move_y:
                list_enemies[0][i].speed = -list_enemies[0][i].speed
        # colisão dos primeiros inimigos
        for i in list_enemies[0]:
            if ball_collision(psg, i):
                psg.x = width / 2
                psg.y = height / 2
                move_x = 0
                move_y = 0
                for extand in range(len(list_walls)):
                    list_walls[extand].x = copy_walls[extand].x
                    list_walls[extand].y = copy_walls[extand].y
                for extand in range(len(list_end_phase)):
                    list_end_phase[extand].x = copy_ways[extand].x
                    list_end_phase[extand].y = copy_ways[extand].y
        # ________________________________________________________________________
        # Fazendo a colisão do personagem com a parede
        for i in list_walls:
            if collision(i, psg):
                psg.x = width / 2
                psg.y = height / 2
                move_x = 0
                move_y = 0
                for extand in range(len(list_walls)):
                    list_walls[extand].x = copy_walls[extand].x
                    list_walls[extand].y = copy_walls[extand].y
                for extand in range(len(list_end_phase)):
                    list_end_phase[extand].x = copy_ways[extand].x
                    list_end_phase[extand].y = copy_ways[extand].y
        if collision(way_one, psg):
            phase_one_part_two()
        if collision(way_two, psg):
            phase_one_part_three()

        # ______________________________________________________ movimentação e colisão do botão
        button.x = button.ini_x + move_x  # movimentação X
        button.y = button.ini_y + move_y  # movimentação Y
        if ball_collision(button, psg):   # Colisão com o personagem
            if wall_17 in list_walls:       # Verifica se há a parede 17 na lista
                list_walls.remove(wall_17)  # Se colidir, retira a parede 17 da lista.
        # _______________________________________________________ move control
        if left_is_down():
            # next_txt += 1
            # esmaecer_white.cont = 0
            # restart_now()
            for i in list_walls:
                i.x += velocity
            for i in list_end_phase:
                i.x += velocity
            move_x += velocity

        if right_is_down():
            for i in list_walls:
                i.x -= velocity
            for i in list_end_phase:
                i.x -= velocity
            move_x -= velocity

        if up_is_down():
            psg.y -= velocity

        if down_is_down():
            psg.y += velocity

        # ___________________________________________________________
        clock.tick(30)
        pygame.display.update()  # Update de tela
        # Evento de saída
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                pygame.display.quit()


# 17,64 + 10,24 + 1,44 + 0,04 + 7,84 + 23,04


def phase_one_part_two():
    black = (0, 0, 0)
    white = (255, 255, 255)
    bg4 = pygame.image.load('data\\images\\bg4.png')
    bg5 = pygame.image.load('data\\images\\bg5.png')
    psg = Persona(width / 2, height / 2, 10)

    list_txt = [["Okay", 50, 2], ["Observe bem o tempo", 30, 3], ["Aprenda... e siga", 50, 4], ["Isso!", 90, 1],
                ["Nem quero pensar", 90, 1], ["O que havia no outro lado", 90, 1]]

    wall_1 = Walls(0, 0, 750, 25, 0)
    wall_2 = Walls(0, 480 - 25, 750, 25, 0)
    wall_3 = Walls(0, 0, 25, 480, 0)
    wall_4 = Walls(750, 0, 750, 25, 0)
    wall_5 = Walls(750, 480 - 25, 750, 25, 0)
    list_walls = [wall_1, wall_2, wall_3, wall_4, wall_5]

    end_game = Walls(1500, 0, 25, 480, 0, (102, 162, 102))
    copy_walls = []
    for i in list_walls:
        copy_wall = Walls(i.x, i.y, i.width, i.height, i.angle)
        copy_walls.append(copy_wall)

    for i in range(20):
        create_ball(0, 0, 1)
        create_ball(0, 0, 2)
        create_ball(0, 0, 3)

    next_txt = 0
    fade = 0
    t1 = 1.0
    velocity = 5
    move_x = 0
    move_y = 0
    clock = pygame.time.Clock()
    close = False
    while not close:
        screen.fill(black)  # Limpa tela
        s.fill((0, 0, 0, 0))  # Limpa a tela da surface S (responsável pelo texto)
        s.set_alpha(fade)  # Define a transparência novamente

        screen.blit(bg4, (0 + move_x, 0 + move_y))  # Background 1 até 7
        screen.blit(bg5, (750 + move_x, 0 + move_y))
        for i in range(len(list_enemies)):
            for n in list_enemies[i]:
                n.draw_obstacle()  # Desenho de todos os inimigos
        for i in list_walls:
            i.draw_wall()  # Desenho de todas as paredes
        end_game.draw_wall()
        # Define o texto, a posição, cor, tamanho e fonte do texto. Desenhando na surface S
        txt(list_txt[next_txt][0], width / 2, height / 2 + 100, white, 45, "imprintshadow")
        screen.blit(s, (0, 0))  # Desenha a surface S na tela (screen)
        pygame.draw.circle(screen, (255, 255, 255), (psg.x, psg.y), psg.rad)  # Desenho do personagem

        # ______________________________________ Aparecer e desaparecer texto
        fade_velocity = list_txt[next_txt][1]
        if 255 >= fade >= 0:
            fade += fade_velocity

        dif = datetime.datetime.now() - now
        if dif.seconds >= list_txt[next_txt][2]:
            if fade > 255:
                fade = 255
                list_txt[next_txt][1] = -list_txt[next_txt][1]
            if fade < 0:
                if -move_x > 700 or next_txt < 2:
                    fade = 0
                    restart_now()
                    if next_txt < len(list_txt)-1:
                        next_txt += 1

        # ___________________________________________________________________ Controle de inimigos
        t1 += 0.001
        for i in range(len(list_enemies[1])):
            list_enemies[1][i].x = 250 * math.cos((t1 * (i + 1)) * 3) * math.cos((t1 * (i + 1))) + 750 + move_x
            list_enemies[1][i].y = 250 * math.cos((t1 * (i + 1)) * 3) * math.sin((t1 * (i + 1))) + 250 + move_y
        for i in range(len(list_enemies[2])):
            list_enemies[2][i].x = 100 * math.cos((t1 * (i + 1)) * 3) * math.cos((t1 * (i + 1))) + 850 + move_x
            list_enemies[2][i].y = 100 * math.cos((t1 * (i + 1)) * 3) * math.sin((t1 * (i + 1))) + 370 + move_y
        for i in range(len(list_enemies[3])):
            list_enemies[3][i].x = 100 * math.cos((t1 * (i + 1)) * 3) * math.cos((t1 * (i + 1))) + 850 + move_x
            list_enemies[3][i].y = 100 * math.cos((t1 * (i + 1)) * 3) * math.sin((t1 * (i + 1))) + 130 + move_y
        # Verificação de colisão com inimigos 2

        for n in range(3):
            for i in list_enemies[n + 1]:
                if ball_collision(psg, i):
                    psg.x = width / 2
                    psg.y = height / 2
                    move_x = 0
                    move_y = 0
                    for extand in range(len(list_walls)):
                        list_walls[extand].x = copy_walls[extand].x
                        list_walls[extand].y = copy_walls[extand].y
                    end_game = Walls(1500, 0, 25, 480, 0, (102, 162, 102))
        # ________________________________________________________________________
        # Fazendo a colisão do personagem com a parede
        for i in list_walls:
            if collision(i, psg):
                psg.x = width / 2
                psg.y = height / 2
                move_x = 0
                move_y = 0
                for n in range(len(list_walls)):
                    list_walls[n].x = copy_walls[n].x
                    list_walls[n].y = copy_walls[n].y
                end_game = Walls(1500, 0, 25, 480, 0, (102, 162, 102))
        if collision(end_game, psg):
            continua()
        # _______________________________________________________ move control
        if left_is_down():
            for i in list_walls:
                i.x += velocity
            end_game.x += velocity
            move_x += velocity

        if right_is_down():
            for i in list_walls:
                i.x -= velocity
            end_game.x -= velocity
            move_x -= velocity

        if up_is_down():
            psg.y -= velocity

        if down_is_down():
            psg.y += velocity

        clock.tick(30)
        pygame.display.update()  # Update de tela
        # Evento de saída
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                pygame.display.quit()


def phase_one_part_three():
    black = (0, 0, 0)
    white = (255, 255, 255)
    bg4 = pygame.image.load('data\\images\\bg4.png')
    bg5 = pygame.image.load('data\\images\\bg5.png')
    psg = Persona(width / 2, height / 2, 10)

    wall_1 = Walls(0, 0, 750, 25, 0)
    wall_2 = Walls(0, 480 - 25, 750, 25, 0)
    wall_3 = Walls(0, 0, 25, 480, 0)
    wall_4 = Walls(750, 0, 750, 25, 0)
    wall_5 = Walls(750, 480 - 25, 750, 25, 0)
    list_walls = [wall_1, wall_2, wall_3, wall_4, wall_5]

    list_txt = [["Não!", 50, 4], ["Era para cima...", 30, 3], ["Isso vai ser difícil...", 50, 4], ["Uhh Boa!", 90, 1],
                ["Mas foi perigoso!", 90, 1], ["Não quero que se machuque...", 90, 1]]

    end_game = Walls(1500, 0, 25, 480, 0, (102, 162, 102))

    copy_walls = []
    for i in list_walls:
        copy_wall = Walls(i.x, i.y, i.width, i.height, i.angle)
        copy_walls.append(copy_wall)

    for i in range(20):
        create_ball(0, 0, 4)

    fade = 0
    next_txt = 0
    t2 = 1.0
    velocity = 5
    move_x = 0
    move_y = 0
    clock = pygame.time.Clock()
    close = False
    while not close:
        screen.fill(black)  # Limpa tela
        s.fill((0, 0, 0, 0))  # Limpa a tela da surface S (responsável pelo texto)
        s.set_alpha(fade)  # Define a transparência novamente

        screen.blit(bg4, (0 + move_x, 0 + move_y))  # Background 1 até 7
        screen.blit(bg5, (750 + move_x, 0 + move_y))
        for n in list_enemies[4]:
            n.draw_obstacle()  # Desenho de todos os inimigos
        for i in list_walls:
            i.draw_wall()  # Desenho de todas as paredes
        end_game.draw_wall()
        txt(list_txt[next_txt][0], width / 2, height / 2 + 100, white, 45, "imprintshadow")
        screen.blit(s, (0, 0))  # Desenha a surface S na tela (screen)
        pygame.draw.circle(screen, (255, 255, 255), (psg.x, psg.y), psg.rad)  # Desenho do personagem

        # ______________________________________ Aparecer e desaparecer texto
        fade_velocity = list_txt[next_txt][1]
        if 255 >= fade >= 0:
            fade += fade_velocity

        dif = datetime.datetime.now() - now
        if dif.seconds >= list_txt[next_txt][2]:
            if fade > 255:
                fade = 255
                list_txt[next_txt][1] = -list_txt[next_txt][1]
            if fade < 0:
                if -move_x > 700 or next_txt < 2:
                    fade = 0
                    restart_now()
                    if next_txt < len(list_txt) - 1:
                        next_txt += 1
        # ______________________________________________________________________ Controle de inimigos
        t2 += 0.00002
        for i in range(len(list_enemies[4])):
            list_enemies[4][i].x = 220 * math.cos((t2 * (i + 1)) * 360) * math.cos((t2 * (i + 1))) + 750 + move_x
            list_enemies[4][i].y = 220 * math.cos((t2 * (i + 1)) * 360) * math.sin((t2 * (i + 1))) + 250 + move_y

        # Colisão de inimigos inferiores
        for i in list_enemies[4]:
            if ball_collision(psg, i):
                psg.x = width / 2
                psg.y = height / 2
                move_x = 0
                move_y = 0
                for extand in range(len(list_walls)):
                    list_walls[extand].x = copy_walls[extand].x
                    list_walls[extand].y = copy_walls[extand].y
                end_game = Walls(1500, 0, 25, 480, 0, (102, 162, 102))

        if collision(end_game, psg):
            continua()
        # ________________________________________________________________________
        # Fazendo a colisão do personagem com a parede
        for i in list_walls:
            if collision(i, psg):
                psg.x = width / 2
                psg.y = height / 2
                move_x = 0
                move_y = 0
                for n in range(len(list_walls)):
                    list_walls[n].x = copy_walls[n].x
                    list_walls[n].y = copy_walls[n].y
                end_game = Walls(1500, 0, 25, 480, 0, (102, 162, 102))

        # _______________________________________________________ move control
        if left_is_down():
            for i in list_walls:
                i.x += velocity
            end_game.x += velocity
            move_x += velocity

        if right_is_down():
            for i in list_walls:
                i.x -= velocity
            end_game.x -= velocity
            move_x -= velocity

        if up_is_down():
            psg.y -= velocity

        if down_is_down():
            psg.y += velocity

        clock.tick(30)
        pygame.display.update()  # Update de tela
        # Evento de saída
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                pygame.display.quit()


def continua():
    restart_now()
    black = (0, 0, 0)
    color_txt = (255, 255, 255)
    clock = pygame.time.Clock()
    fade = 0
    fade_velocity = 5
    close = False
    while not close:
        screen.fill(black)  # Limpa tela
        s.fill((0, 0, 0, 0))
        s.set_alpha(fade)
        txt("Continua...", width / 2, height / 2, color_txt, 45, "imprintshadow")
        screen.blit(s, (0, 0))
        """
        for i in pygame.font.get_fonts():
            print(i)
        """
        if 255 >= fade >= 0:
            fade += fade_velocity

        if enter_is_down():
            if fade > 255:
                fade = 255
            if fade < 0:
                fade = 0
            fade_velocity = fade_velocity
        clock.tick(30)
        pygame.display.update()  # Update de tela
        # Evento de saída
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                pygame.display.quit()


"""
def ger_phase():  # Gerenciador de fase
    part = 0
    phases_list = [[phase_one_part_one(), phase_one_part_two(), phase_one_part_three()], [continua()]]
    close = 1
    while close != 0:
        phases_list[Gphase][part]
        part = phases_list[Gphase][part]
        if part >= 10:
            close = 0
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    size = width, height = 750, 480
    screen = pygame.display.set_mode(size)
    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.set_alpha(255)
    # ger_phase()
    phase_one_part_one()
    # phase_one_part_two()
    # phase_one_part_three()
    # continua()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
