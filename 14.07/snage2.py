# screen -> oyna
# snake -> ilon
# moving -> qimirlash
# add -> qo'shish
# food -> ovqat
# score -> achko
# quit -> chiqish
# game -> o'yin tugadi

# 1. pygame ni ustanovka qildik
# 2. oyna yaratish

""" 1 - qism oyna yaratish"""
# import pygame
# pygame.init()
# dis = pygame.display.set_mode((400, 300))
# pygame.display.update()
# pygame.quit()
# quit()

""" oynani ushlab turish """

# import pygame
#
# pygame.init()
# dis = pygame.display.set_mode((400, 300))
# pygame.display.update()
# pygame.display.set_caption('mening birinchi o\'yinim')
# game_over = False
# while not game_over:
#     for event in pygame.event.get():  # event bu xodisalar
#         print(event)  # prints out all the actions that take place on the screen
#
# pygame.quit()
# quit()

""" 2 - qism oynani o'chirish tugmasini faollantirish"""
# import pygame
#
# pygame.init()
# dis = pygame.display.set_mode((400, 300))
# pygame.display.update()
# pygame.display.set_caption('Snake game by Edureka')
# game_over = False
# while not game_over:
#     for event in pygame.event.get():  # barcha hodisalarni olish
#         if event.type == pygame.QUIT:  # agar x tugma bosilsa game over = true bo'lsin
#             game_over = True
#
# pygame.quit()  # Pygamedan chiqish
# quit()  # bu  dasturdan chiqish

""" 3 - qism Ilon yaratish """
# import pygame
#
# pygame.init()
# dis = pygame.display.set_mode((400, 300))
#
# pygame.display.set_caption('ilon')
#
# blue = (0, 0, 255)
# red = (255, 0, 0)
#
# game_over = False
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#     pygame.draw.rect(dis, blue, [200, 150, 10, 10])
#     # pygame.draw.rect(ekran, rang, [x_kor, y_kor, x_o'lcham, y_o'lcham]) rect - to'trburchak
#     pygame.display.update()
# pygame.quit()
# quit()

""" 4 - ilonni qimirlatish """
# import pygame
#
# pygame.init()
#
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
#
# dis = pygame.display.set_mode((800, 600))
# pygame.display.set_caption('Snake Game by Edureka')
#
# game_over = False
#
# x1 = 300
# y1 = 300
#
# x1_change = 0
# y1_change = 0
#
# clock = pygame.time.Clock()
#
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 x1_change = -10
#                 y1_change = 0
#             elif event.key == pygame.K_RIGHT:
#                 x1_change = 10
#                 y1_change = 0
#             elif event.key == pygame.K_UP:
#                 y1_change = -10
#                 x1_change = 0
#             elif event.key == pygame.K_DOWN:
#                 y1_change = 10
#                 x1_change = 0
#
#     x1 += x1_change
#     y1 += y1_change
#     dis.fill(white)
#     pygame.draw.rect(dis, black, [x1, y1, 10, 10])
#
#     pygame.display.update()
#
#     clock.tick(10)
#
# pygame.quit()
# quit()

""" 5 - qism """
# import pygame
# import time
#
# pygame.init()
#
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
#
# dis_width = 800
# dis_height = 600
# dis = pygame.display.set_mode((dis_width, dis_width))
# pygame.display.set_caption('Ilon o\'yin')
#
# game_over = False
#
# x1 = dis_width / 2
# y1 = dis_height / 2
#
# snake_block = 10
#
# x1_change = 0
# y1_change = 0
#
# clock = pygame.time.Clock()
# snake_speed = 30
#
# font_style = pygame.font.SysFont(None, 50)
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 2, dis_height / 2])
#
#
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 x1_change = -snake_block
#                 y1_change = 0
#             elif event.key == pygame.K_RIGHT:
#                 x1_change = snake_block
#                 y1_change = 0
#             elif event.key == pygame.K_UP:
#                 y1_change = -snake_block
#                 x1_change = 0
#             elif event.key == pygame.K_DOWN:
#                 y1_change = snake_block
#                 x1_change = 0
#
#     if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#         game_over = True
#
#     x1 += x1_change
#     y1 += y1_change
#     dis.fill(white)
#     pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
#
#     pygame.display.update()
#
#     clock.tick(snake_speed)
#
# message("yutqazdingiz", red)
# pygame.display.update()
# time.sleep(2)
#
# pygame.quit()
# quit()

"""6 - qism: ovqat qo'shish """
# import pygame
# import time
# import random
#
# pygame.init()
#
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# blue = (0, 0, 255)
#
# dis_width = 800
# dis_height = 600
#
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Ilon o\'yin')
#
# clock = pygame.time.Clock()
#
# snake_block = 10
# snake_speed = 30
#
# font_style = pygame.font.SysFont(None, 30)
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 3, dis_height / 3])
#
#
# def gameLoop():  # creating a function
#     game_over = False
#     game_close = False
#
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#
#     x1_change = 0
#     y1_change = 0
#
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#
#     while not game_over:
#
#         while game_close == True:
#             dis.fill(white)
#             message("Yutqazdingiz! Q - chiqish; C - davom ettirish", red)
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(white)
#         pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
#         pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
#         pygame.display.update()
#
#         if x1 == foodx and y1 == foody:
#             print("ovqatlandi!!")
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
#
# gameLoop()

""" 7 - qism. ilon uzunligi """
# import pygame
# import time
# import random
#
# pygame.init()
#
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
#
# dis_width = 600
# dis_height = 400
#
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game by Edureka')
#
# clock = pygame.time.Clock()
#
# snake_block = 10
# snake_speed = 15
#
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
#
#
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
#
#
# def gameLoop():
#     game_over = False
#     game_close = False
#
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#
#     x1_change = 0
#     y1_change = 0
#
#     snake_List = []
#     Length_of_snake = 1
#
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#
#     while not game_over:
#
#         while game_close == True:
#             dis.fill(blue)
#             message("You Lost! Press C-Play Again or Q-Quit", red)
#
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
#
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
#
#         our_snake(snake_block, snake_List)
#
#         pygame.display.update()
#
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
#
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
#
# gameLoop()

""" 8 - qism """

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Ilon o'yini")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Achko: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def block():
    pygame.draw.rect(dis, green, [dis_width/2, dis_height/2, 50, 150])
    pygame.draw.rect(dis, green, [dis_width / 2, dis_height / 2, 150, 50])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            block.fit()
            message("Yutqazdingiz! C - Davom etish; Q - chiqish", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width
        if y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height
        # if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #     game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        block()
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()