#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from time import sleep  # sleepを使うため
import sys
import os
import random  # 乱数を得るためのimport

SCREEN_SIZE = (1280, 720)  # スクリーンのサイズを決める変数
# グローバル変数
Card1 = [0, 0, 0, 0, 0]
cardimage = ['back.png', 'back.png', 'back.png', 'back.png', 'back.png']
holdchange = [0, 0, 0, 0, 0]
HIGH = (0, 0)
Basyo = (0, 0)
shaful = 0
rank = 'a'
ranknum = 0

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(u"トランプゲーム")


def load_image(filename, colorkey=None, use_cardsize=True):
    """
    画像を読み込むための関数
    """

    # ファイルパスを作成し，カードを読み込む
    filename = os.path.join("carddata", filename)
    try:
        image = pygame.image.load(filename)
    # パスが正しくなかった場合は終了する
    except pygame.error:
        print("Cannot load image:")
        raise SystemExit

    image = image.convert()

    # カード画像を表示する際は，自動的にサイズを調整する
    if use_cardsize:
        image = pygame.transform.scale(image, (218, 320))

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


def decidecard():
    """
    配布するカードを決定する関数
    """
    counter = 0
    check1 = 0
    check2 = 0
    global shaful
    cardimage
    num = 0

    if shaful == 1:
        counter = 0
        while True:
            if holdchange[counter] == 1:
                Card1[counter] = (random.randint(0, 51))  # カードを決める
            counter += 1
            if counter == 5:
                break

    elif shaful == 0:
        counter = 0
        while True:
            Card1[counter] = (random.randint(0, 51))  # カードを決める
            counter += 1
            if counter == 5:
                break

    while True:
        if Card1[1] == Card1[0]:
            if holdchange[1] == 0:
                Card1[1] = (random.randint(0, 51))  # カードを決める
        if Card1[1] != Card1[0]:
            break

    while True:
        if Card1[2] == Card1[0] or Card1[2] == Card1[1]:
            if holdchange[2] == 0:
                Card1[2] = (random.randint(0, 51))  # カードを決める
        if Card1[2] != Card1[0] and Card1[2] != Card1[1]:
            break

    while True:
        if Card1[3] == Card1[0] or Card1[3] == Card1[1] or Card1[3] == Card1[2]:
            if holdchange[3] == 0:
                Card1[3] = (random.randint(0, 51))  # カードを決める
        if Card1[3] != Card1[0] and Card1[3] != Card1[1] and Card1[3] != Card1[2]:
            break

    while True:
        if Card1[4] == Card1[0] or Card1[4] == Card1[1] or Card1[4] == Card1[2] or Card1[4] == Card1[3]:
            if holdchange[4] == 0:
                Card1[4] = (random.randint(0, 51))  # カードを決める
        if Card1[4] != Card1[0] and Card1[4] != Card1[1] and Card1[4] != Card1[2] and Card1[4] != Card1[3]:
            break

    while True:  # 得られた乱数の結果により画像を決定するif文
        if Card1[num] == 0:
            cardimage[num] = load_image('h1.png')
        elif Card1[num] == 1:
            cardimage[num] = load_image('h2.png')
        elif Card1[num] == 2:
            cardimage[num] = load_image('h3.png')
        elif Card1[num] == 3:
            cardimage[num] = load_image('h4.png')
        elif Card1[num] == 4:
            cardimage[num] = load_image('h5.png')
        elif Card1[num] == 5:
            cardimage[num] = load_image('h6.png')
        elif Card1[num] == 6:
            cardimage[num] = load_image('h7.png')
        elif Card1[num] == 7:
            cardimage[num] = load_image('h8.png')
        elif Card1[num] == 8:
            cardimage[num] = load_image('h9.png')
        elif Card1[num] == 9:
            cardimage[num] = load_image('h10.png')
        elif Card1[num] == 10:
            cardimage[num] = load_image('h11.png')
        elif Card1[num] == 11:
            cardimage[num] = load_image('h12.png')
        elif Card1[num] == 12:
            cardimage[num] = load_image('h13.png')
        elif Card1[num] == 13:
            cardimage[num] = load_image('d1.png')
        elif Card1[num] == 14:
            cardimage[num] = load_image('d2.png')
        elif Card1[num] == 15:
            cardimage[num] = load_image('d3.png')
        elif Card1[num] == 16:
            cardimage[num] = load_image('d4.png')
        elif Card1[num] == 17:
            cardimage[num] = load_image('d5.png')
        elif Card1[num] == 18:
            cardimage[num] = load_image('d6.png')
        elif Card1[num] == 19:
            cardimage[num] = load_image('d7.png')
        elif Card1[num] == 20:
            cardimage[num] = load_image('d8.png')
        elif Card1[num] == 21:
            cardimage[num] = load_image('d9.png')
        elif Card1[num] == 22:
            cardimage[num] = load_image('d10.png')
        elif Card1[num] == 23:
            cardimage[num] = load_image('d11.png')
        elif Card1[num] == 24:
            cardimage[num] = load_image('d12.png')
        elif Card1[num] == 25:
            cardimage[num] = load_image('d13.png')
        elif Card1[num] == 26:
            cardimage[num] = load_image('s1.png')
        elif Card1[num] == 27:
            cardimage[num] = load_image('s2.png')
        elif Card1[num] == 28:
            cardimage[num] = load_image('s3.png')
        elif Card1[num] == 29:
            cardimage[num] = load_image('s4.png')
        elif Card1[num] == 30:
            cardimage[num] = load_image('s5.png')
        elif Card1[num] == 31:
            cardimage[num] = load_image('s6.png')
        elif Card1[num] == 32:
            cardimage[num] = load_image('s7.png')
        elif Card1[num] == 33:
            cardimage[num] = load_image('s8.png')
        elif Card1[num] == 34:
            cardimage[num] = load_image('s9.png')
        elif Card1[num] == 35:
            cardimage[num] = load_image('s10.png')
        elif Card1[num] == 36:
            cardimage[num] = load_image('s11.png')
        elif Card1[num] == 37:
            cardimage[num] = load_image('s12.png')
        elif Card1[num] == 38:
            cardimage[num] = load_image('s13.png')
        elif Card1[num] == 39:
            cardimage[num] = load_image('c1.png')
        elif Card1[num] == 40:
            cardimage[num] = load_image('c2.png')
        elif Card1[num] == 41:
            cardimage[num] = load_image('c3.png')
        elif Card1[num] == 42:
            cardimage[num] = load_image('c4.png')
        elif Card1[num] == 43:
            cardimage[num] = load_image('c5.png')
        elif Card1[num] == 44:
            cardimage[num] = load_image('c6.png')
        elif Card1[num] == 45:
            cardimage[num] = load_image('c7.png')
        elif Card1[num] == 46:
            cardimage[num] = load_image('c8.png')
        elif Card1[num] == 47:
            cardimage[num] = load_image('c9.png')
        elif Card1[num] == 48:
            cardimage[num] = load_image('c10.png')
        elif Card1[num] == 49:
            cardimage[num] = load_image('c11.png')
        elif Card1[num] == 50:
            cardimage[num] = load_image('c12.png')
        elif Card1[num] == 51:
            cardimage[num] = load_image('c13.png')
        else:
            cardimage[num] = load_image('joker.png')

        num += 1
        if num == 5:
            break  # 五回表示したら終了

# decidecard関数定義終了


def rank_check():
    global rank
    global ranknum
    ranknum = 0
    pare1 = 0
    pare2 = 0
    pare3 = 0
    pare4 = 0
    pare5 = 0
    pare6 = 0
    pare7 = 0
    pare8 = 0
    pare9 = 0
    pare10 = 0
    devided_card0 = 0
    devided_card1 = 0
    devided_card2 = 0
    devided_card3 = 0
    devided_card4 = 0
    carddata = [0, 0, 0, 0, 0]
    line = [0, 0, 0, 0]

    carddata = Card1

    devided_card0 = carddata[0] % 13
    devided_card1 = carddata[1] % 13
    devided_card2 = carddata[2] % 13
    devided_card3 = carddata[3] % 13
    devided_card4 = carddata[4] % 13

    line[0] = devided_card4 - devided_card3
    line[1] = devided_card3 - devided_card2
    line[2] = devided_card2 - devided_card1
    line[3] = devided_card1 - devided_card0

    pare1 = devided_card4 - devided_card3
    pare2 = devided_card4 - devided_card2
    pare3 = devided_card4 - devided_card1
    pare4 = devided_card4 - devided_card0
    pare5 = devided_card3 - devided_card2
    pare6 = devided_card3 - devided_card1
    pare7 = devided_card3 - devided_card0
    pare8 = devided_card2 - devided_card1
    pare9 = devided_card2 - devided_card0
    pare10 = devided_card1 - devided_card0

    if pare1 == 0:
        ranknum += 1
    if pare2 == 0:
        ranknum += 1
    if pare3 == 0:
        ranknum += 1
    if pare4 == 0:
        ranknum += 1
    if pare5 == 0:
        ranknum += 1
    if pare6 == 0:
        ranknum += 1
    if pare7 == 0:
        ranknum += 1
    if pare8 == 0:
        ranknum += 1
    if pare9 == 0:
        ranknum += 1
    if pare10 == 0:
        ranknum += 1

    if line[0] == 1 and line[1] == 1 and line[2] == 1 and line[3] == 1:
        ranknum = 5

    if Card1[0] < 13 and Card1[1] < 13 and Card1[2] < 13 and Card1[3] < 13 and Card1[4] < 13:
        ranknum = 10

    if Card1[0] < 26 and Card1[1] < 26 and Card1[2] < 26 and Card1[3] < 26 and Card1[4] < 26:
        if Card1[0] >= 13 and Card1[1] >= 13 and Card1[2] >= 13 and Card1[3] >= 13 and Card1[4] >= 13:
            ranknum = 10

    if Card1[0] < 39 and Card1[1] < 39 and Card1[2] < 39 and Card1[3] < 39 and Card1[4] < 39:
        if Card1[0] >= 26 and Card1[1] >= 26 and Card1[2] >= 26 and Card1[3] >= 26 and Card1[4] >= 26:
            ranknum = 10

    if Card1[0] >= 39 and Card1[1] >= 39 and Card1[2] >= 39 and Card1[3] >= 39 and Card1[4] >= 39:
        ranknum = 10

    if carddata[0] == 0 and carddata[1] == 9 and carddata[2] == 10 and carddata[3] == 11 and carddata[4] == 12:
        ranknum = 100

    if carddata[0] == 13 and carddata[1] == 22 and carddata[2] == 23 and carddata[3] == 24 and carddata[4] == 25:
        ranknum = 100
    if carddata[0] == 26 and carddata[1] == 35 and carddata[2] == 36 and carddata[3] == 37 and carddata[4] == 38:
        ranknum = 100
    if carddata[0] == 39 and carddata[1] == 48 and carddata[2] == 49 and carddata[3] == 50 and carddata[4] == 51:
        ranknum = 100

    if ranknum == 0:
        rank = load_image("buta.png", use_cardsize=False)
    elif ranknum == 1:
        rank = load_image("onepare.png", use_cardsize=False)
    elif ranknum == 2:
        rank = load_image("twopare.png", use_cardsize=False)
    elif ranknum == 3:
        rank = load_image("threecard.png", use_cardsize=False)
    elif ranknum == 4:
        ranknum = 20
        rank = load_image("fulhouse.png", use_cardsize=False)
    elif ranknum == 5:
        rank = load_image("line.png", use_cardsize=False)
    elif ranknum == 6:
        ranknum = 40
        rank = load_image("fourcard.png", use_cardsize=False)
    elif ranknum == 10:
        rank = load_image("fulash.png", use_cardsize=False)
        if line[0] == 1 and line[1] == 1 and line[2] == 1 and line[3] == 1:
            ranknum = 70
            rank = load_image("linefulash.png", use_cardsize=False)
    elif ranknum == 100:
        rank = load_image("royal.png", use_cardsize=False)

    print(ranknum)


def doubleup():

    global ranknum


def print_cards():  # PRINT関数の定義　
    num = 0
    global rank
    cardimage
    # イメージを用意
    backImg = load_image("aozora-1280x720.jpg", use_cardsize=False)  # タイトル、背景等
    # now = load_image("now.png", use_cardsize=False)
    Hold = load_image("hold.png", use_cardsize=False)  # Holdをカードの下に表示
    # Change = load_image("change.png", use_cardsize=False)  # changeをカードの下に表示
    screen.blit(backImg, (0, 0))
    screen.blit(rank, (60, 20))
    while True:
        screen.blit(cardimage[num], ((num * 230 + 80), 350))  # 五回カードを表示
        screen.blit(Hold, ((num * 230 + 100), 670))
        num += 1
        if num == 5:  # 五回表示したら終了
            break

    pygame.display.update()


def first_check():
    global shaful
    global ranknum

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_RETURN:  # ENTERキーが入力されたとき
                    shaful = 1
                    decidecard()  # カードの再シャッフル
                    rank_check()
                    print_cards()  # 再表示

                    holdchange[4] = 0
                    holdchange[3] = 0
                    holdchange[2] = 0
                    holdchange[1] = 0
                    holdchange[0] = 0

                    # sleep(3)
                    # if event.key == K_RETURN :
                    # 	if ranknum > 0:
                    # 		doubleup()
                    # 	else :
                    # 		sys.exit()
                    # break		#first_check関数から抜ける

        if event.type == MOUSEBUTTONDOWN:  # もしマウスをクリックしたら
            (x, y) = event.pos
            Basyo = (x, y)
            if y >= 300:
                if x >= 1000:  # 5枚目の画像のあたりをクリックした場合
                    if holdchange[4] == 0:
                        screen.blit(load_image(
                            "change.png", use_cardsize=False), (1020, 670))
                        holdchange[4] = 1
                    elif holdchange[4] == 1:
                        screen.blit(load_image(
                            "hold.png", use_cardsize=False), (1020, 670))
                        holdchange[4] = 0

                if x >= 770 and x < 1000:  # 4枚目の画像のあたりをクリックした場合
                    if holdchange[3] == 0:
                        screen.blit(load_image(
                            "change.png", use_cardsize=False), (790, 670))
                        holdchange[3] = 1
                    elif holdchange[3] == 1:
                        screen.blit(load_image(
                            "hold.png", use_cardsize=False), (790, 670))
                        holdchange[3] = 0

                if x >= 550 and x < 770:  # 3枚目の画像のあたりをクリックした場合
                    if holdchange[2] == 0:
                        screen.blit(load_image(
                            "change.png", use_cardsize=False), (560, 670))
                        holdchange[2] = 1
                    elif holdchange[2] == 1:
                        screen.blit(load_image(
                            "hold.png", use_cardsize=False), (560, 670))
                        holdchange[2] = 0

                if x >= 300 and x < 550:  # 2枚目の画像のあたりをクリックした場合
                    if holdchange[1] == 0:
                        screen.blit(load_image(
                            "change.png", use_cardsize=False), (330, 670))
                        holdchange[1] = 1
                    elif holdchange[1] == 1:
                        screen.blit(load_image(
                            "hold.png", use_cardsize=False), (330, 670))
                        holdchange[1] = 0

                if x >= 100 and x < 300:  # 1枚目の画像のあたりをクリックした場合
                    if holdchange[0] == 0:
                        screen.blit(load_image(
                            "change.png", use_cardsize=False), (100, 670))
                        holdchange[0] = 1
                    elif holdchange[0] == 1:
                        screen.blit(load_image(
                            "hold.png", use_cardsize=False), (100, 670))
                        holdchange[0] = 0
            pygame.display.update()
            sleep(0.2)


if __name__ == "__main__":
    decidecard()  # PRINT関数とrank_check関数より前に一度実行する必要がある。
    rank_check()
    print_cards()
    first_check()
