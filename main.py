# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *
from edit_image_class import edit_image

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450




def main():
    # Pygameの初期化
    pygame.init()
    # 画面設定
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    screen = pygame.display.get_surface()

    santa = pygame.image.load("image/magao.png").convert_alpha()
    #元サイズ　975, 673
    santa = edit_image().resize(santa,700)
    santa_rect = santa.get_rect()



    #サンタ画像の初期位置
    santa_rect.center = (350, 250)

    running = True  # ループ処理の実行を継続するフラグ

    while running:
        # 画面更新
        pygame.display.update()  
        # 更新間隔（30msec）           
        pygame.time.wait(30)
        # 画面の背景色（RGBA）     
        screen.fill((0, 0, 0, 0))
        screen.blit(santa, santa_rect)  


        # イベント処理
        for event in pygame.event.get():
            # 閉じるボタンが押されたら終了
            if event.type == QUIT: 
                running = False
            # キーイベント
            if event.type == KEYDOWN:
                # Escキーが押されたら終了
                if event.key == K_ESCAPE:   
                    running = False
                if event.key == K_a:
                    santa = pygame.image.load("image/choitoro.png").convert_alpha()
                    santa = edit_image().resize(santa,700)
               
    # Pygameとプログラムの実行を終了
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()