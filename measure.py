# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *
SCREEN_WIDTH = 780
SCREEN_HEIGHT = 650
SANTA_IMG_PATH =  "image/santa_hansin.png"


# Pygameの初期化
pygame.init()
# 画面設定
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
screen = pygame.display.get_surface()


player = pygame.image.load(SANTA_IMG_PATH).convert_alpha()
player_rect = player.get_rect()
print(player_rect)
pygame.quit()

#<rect(0, 0, 746, 875)>
#<rect(0, 0, 746, 852)>
#hansin <rect(0, 0, 975, 673)>