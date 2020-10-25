import pygame as pg
import sys
from Pygame.constants import *

pg.init()

display_width = 800
display_height = 600

screen = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('Demo - PokeMood')

clock = pg.time.Clock()
crashed = False

second_surface = pg.Surface((800, 600))
base_font = pg.font.SysFont("roboto mono", 30, True)

bg = pg.image.load("Background_forest.jpg").convert()
background = pg.transform.scale(bg, (800, 600))
screen.blit(background, (0, 0))

# logo = pg.image.load("LOGO2.PNG")
# logo = pg.transform.scale(logo, (300, 185))

shield = pg.image.load("shield_white.png")
sword = pg.image.load("sword_resized.png")


def text_input(input_rect, user_text):
    pg.draw.rect(screen, BLACK, input_rect, 2)
    pg.draw.rect(screen, COLOR_LIGHT_SELECTED, [72.6, 537.5, 197, 37])
    text_surface = base_font.render(user_text, True, BLACK)
    screen.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))


def vs_logo():
    vs_sign = pg.image.load("VS.PNG")
    vs_sign = pg.transform.scale(vs_sign, (200,150))
    screen.blit(vs_sign, (300, 225))


def text_speech(screen, font: str, size: int, text: str, color, x, y, bold: bool):
    font = pg.font.Font(font, size)
    font.set_bold(bold)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def Aggressive_Ada(x, y, a ,b):
    pink_dragon = pg.image.load('Pink_dragon_01.png').convert_alpha()
    screen.blit(pink_dragon, (x, y))
    text_speech(screen, "RobotoSlab-Medium.ttf", 15, "Aggressive Ada", RED, a, b, True)
    text_speech(screen, "RobotoSlab-Medium.ttf", 15, "Stats: HP: 123, Attack: 20, Mood: Angry", WHITE, 630, 575,
                True)


def Happy_Hasse(x, y, a, b):
    green_monster = pg.image.load('Green_monster_resized.png').convert_alpha()
    screen.blit(green_monster, (x, y))
    text_speech(screen, "RobotoSlab-Medium.ttf", 15, "Happy Hasse", BLUE, a, b, True)
    text_speech(screen, "RobotoSlab-Medium.ttf", 15, "Stats: HP: 113, Attack: 20, Mood: Happy", WHITE, 170, 20,
                True)


def quit_button(mouse):
    text = base_font.render('QUIT', True, BLACK)
    if 650 <= mouse[0] <= 650 + 140 and 30 <= mouse[1] <= 30 + 40:
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, [652, 32, 137, 37])
        pg.draw.rect(screen, BLACK, [650, 30, 140, 40], 3)
    else:
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, [650, 30, 140, 40])
        pg.draw.rect(screen, BLACK, [650, 30, 140, 40], 3)
    screen.blit(text, (690, 40))


def battle_time_button(mouse):
    if 275 <= mouse[0] <= 275 + 240 and 245 <= mouse[1] <= 225 + 100:
        pg.draw.rect(screen, BLACK, (285, 245, 225, 70), 3)
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, (287, 247, 221, 66))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "Battle time!", BLACK, display_width / 2.02,
                    display_height / 2.15, True)
    else:
        pg.draw.rect(screen, BLACK, (285, 245, 225, 70), 3)
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, (287, 247, 221, 66))
        text_speech(screen, "RobotoSlab-Black.ttf", 30, "Battle time!", BLACK, display_width / 2.02,
                    display_height / 2.15, True)


def back_button(mouse):
    if 30 <= mouse[0] <= 30 + 140 and 540 <= mouse[1] <= 540 + 40:
        pg.draw.rect(screen, COLOR_LIGHT_SELECTED, [32, 542, 137, 37])
        pg.draw.rect(screen, BLACK, [30, 540, 140, 40], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "BACK", BLACK, 97, 558, True)
    else:
        pg.draw.rect(screen, COLOR_LIGHT_UNSELECTED, [32, 542, 137, 37])
        pg.draw.rect(screen, BLACK, [30, 540, 140, 40], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "BACK", BLACK, 97, 558, True)


def attack_button(mouse):
    if 200 <= mouse[0] <= 200 + 150 and 430 <= mouse[1] <= 430 + 50:
        pg.draw.rect(screen, LIGHT_RED_SELECTED, [202, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [200, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Attack", BLACK, 272, 453, True)
    else:
        pg.draw.rect(screen, LIGHT_RED_UNSELECTED , [202, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [200, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Attack", BLACK, 272, 453, True)


def block_button(mouse):
    if 445 <= mouse[0] <= 445 + 150 and 430 <= mouse[1] <= 430 + 50:
        pg.draw.rect(screen, LIGHT_BLUE_SELECTED, [447, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [445, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Block", BLACK, 517, 453, True)
    else:

        pg.draw.rect(screen, LIGHT_BLUE_UNSELECTED, [447, 432, 147, 47])
        pg.draw.rect(screen, BLACK, [445, 430, 150, 50], 3)
        text_speech(screen, "RobotoSlab-Black.ttf", 25, "Block", BLACK, 517, 453, True)


def chat_bubble_left():
    left = pg.image.load('Chat_bubble_left.png').convert()
    left_small = pg.transform.scale(left, (300, 170))
    second_surface.blit(left_small, (250, 50))
    text_speech(second_surface, "RobotoSlab-Medium.ttf", 15, "Moodscore: 113", BLACK, 390, 135, True)


def chat_bubble_right():
    right = pg.image.load('Chat_bubble_right.png').convert()
    right_small = pg.transform.scale(right, (300, 170))
    second_surface.blit(right_small, (260, 350))
    text_speech(second_surface, "RobotoSlab-Medium.ttf", 15, "Moodscore: 123", BLACK, 370, 435, True)


button = 0
click = False

def battle_menu():
    global button
    # active = False
    # user_text = ''
    while True:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        Aggressive_Ada(520, 300, 640, 300)
        Happy_Hasse(8, 30, 122, 45)
        screen.blit(second_surface, (0, 0))

        mx, my = pg.mouse.get_pos()
        mouse = pg.mouse.get_pos()

        battle_button_rect = pg.Rect(285, 245, 225, 70)
        battle_time_button(mouse)

        quit_button_rect = pg.Rect(650, 30, 140, 40)
        quit_button(mouse)

        # input_rect = pg.Rect(70, 535, 200, 40)
        # text_input(input_rect, user_text,)

        text_speech(screen, "RobotoSlab-Medium.ttf", 15, "Press [enter] for moodscores", BLACK, 397, 330, True)

        if battle_button_rect.collidepoint((mx, my)):
            if click:
                battle_time()

        if quit_button_rect.collidepoint((mx, my)):
            if click:
                pg.quit()
                sys.exit()

        if button == 1:
            chat_bubble_left()

        if button == 2:
            chat_bubble_right()

        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_RETURN:
                    button += 1

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            # if event.type == pg.MOUSEBUTTONDOWN:
            #     if input_rect.collidepoint(event.pos):
            #         active = True
            #     else:
            #         active = False

            # if event.type == pg.KEYDOWN:
            #     keys = pg.key.get_pressed()
            #     if active:
            #         if keys[pg.K_BACKSPACE]:
            #             user_text = user_text[:-1]
            #         else:
            #             user_text += event.unicode

        pg.display.update()
        clock.tick(60)


def battle_time():
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        Aggressive_Ada(display_width * 0.63, display_height * 0.26, 650, 550)
        Happy_Hasse(display_width * 0.03, display_height * 0.24, 122, 45)
        mouse = pg.mouse.get_pos()
        vs_logo()
        quit_button_rect = pg.Rect(650, 30, 140, 40)
        quit_button(mouse)

        back_button_rect = pg.Rect(30, 540, 140, 40)
        back_button(mouse)

        attack_button_rect = pg.Rect(200, 430, 150, 50)
        attack_button(mouse)

        block_button_rect = pg.Rect(445, 430, 150, 50)
        block_button(mouse)

        mx, my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint((mx, my)):
                    battle_menu()
                if quit_button_rect.collidepoint((mx, my)):
                    pg.quit()
                if block_button_rect.collidepoint((mx, my)):
                    block_func()
                if attack_button_rect.collidepoint((mx, my)):
                    attack_func()

        pg.display.update()
        clock.tick(60)


def block_func():
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        Aggressive_Ada(display_width * 0.63, display_height * 0.26, 650, 550)
        Happy_Hasse(display_width * 0.03, display_height * 0.24, 122, 45)
        screen.blit(shield, (305, 160))
        mouse = pg.mouse.get_pos()

        quit_button_rect = pg.Rect(650, 30, 140, 40)
        quit_button(mouse)

        back_button_rect = pg.Rect(30, 540, 140, 40)
        back_button(mouse)

        attack_button_rect = pg.Rect(200, 430, 150, 50)
        attack_button(mouse)

        block_button_rect = pg.Rect(445, 430, 150, 50)
        block_button(mouse)

        mx, my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint((mx, my)):
                    battle_menu()
                if quit_button_rect.collidepoint((mx, my)):
                    pg.quit()
                if attack_button_rect.collidepoint((mx, my)):
                    attack_func()

        pg.display.update()
        clock.tick(60)


def attack_func():
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        Aggressive_Ada(display_width * 0.63, display_height * 0.26, 650, 550)
        Happy_Hasse(display_width * 0.03, display_height * 0.24, 122, 45)
        screen.blit(sword, (315,170))
        mouse = pg.mouse.get_pos()

        quit_button_rect = pg.Rect(650, 30, 140, 40)
        quit_button(mouse)

        back_button_rect = pg.Rect(30, 540, 140, 40)
        back_button(mouse)

        attack_button_rect = pg.Rect(200, 430, 150, 50)
        attack_button(mouse)

        block_button_rect = pg.Rect(445, 430, 150, 50)
        block_button(mouse)

        mx, my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint((mx, my)):
                    battle_menu()
                if quit_button_rect.collidepoint((mx, my)):
                    pg.quit()
                if block_button_rect.collidepoint((mx, my)):
                    block_func()

        pg.display.update()
        clock.tick(60)

battle_menu()