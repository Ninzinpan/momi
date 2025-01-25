# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *

# 画面サイズ
SCREEN_WIDTH = 1600/2
SCREEN_HEIGHT = 900/2

# プレイヤーの画像ファイルパス
PLAYER_IMG_PATH = "image/player.png"
SANTA_IMG_PATH ="image/santa_stand.png"


# 背景の画像ファイルパス
BACKGROUND_IMG_PATH = "image/background.png"

def main():
    # Pygameの初期化
    pygame.init()
    # 画面設定
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    screen = pygame.display.get_surface()


    # 背景画像の取得
    bg = pygame.image.load(BACKGROUND_IMG_PATH).convert_alpha()
    bg_rect = bg.get_rect()

    # プレイヤー画像の取得
    player = pygame.image.load(PLAYER_IMG_PATH).convert_alpha()
    player_rect = player.get_rect()

    # プレイヤー画像の初期位置
    player_rect.center = (0, 0) 

    # サンタ画像の取得
    #santa = pygame.image.load(SANTA_IMG_PATH).convert_alpha()
    #santa = pygame.transform.scale(santa,(746, 852))
    #santa_rect = santa.get_rect()

    santa = pygame.image.load("image/santa_hansin.png").convert_alpha()
    #元サイズ　975, 673
    santa = pygame.transform.smoothscale(santa,(650, 449))
    santa_rect = santa.get_rect()


    santa_egao = pygame.image.load("image/santa_hyojo_egao.png").convert_alpha()
    orig_x = santa_egao.get_width()
    orig_y = santa_egao.get_height()

    santa_egao = pygame.transform.smoothscale(santa_egao,(orig_x/1.5, orig_y/1.5))
    egao_rect = santa_egao.get_rect()

    #サンタ画像の初期位置
    egao_rect.center = (santa_rect.x,santa_rect.y) 




    running = True  # ループ処理の実行を継続するフラグ

    while running:
        # 画面更新
        pygame.display.update()  
        # 更新間隔（30msec）           
        pygame.time.wait(30)
        # 画面の背景色（RGBA）     
        screen.fill((100, 0, 0, 0))

        # プレイヤーが画面の範囲外に出ないための処理
        # 左端のx座標が0より小さければ0にする 
        if player_rect.left < 0:
            player_rect.left = 0
        # 右端のx座標が画面の幅より大きければ画面左端までにする
        if player_rect.right > SCREEN_WIDTH:
            player_rect.right = SCREEN_WIDTH
        # 上端のy座標が0より小さければ0にする 
        if player_rect.top < 0:
            player_rect.top = 0
        # 下端のy座標が画面の高さより大きければ画面下端までにする
        if player_rect.bottom > SCREEN_HEIGHT:
            player_rect.bottom = SCREEN_HEIGHT 

        # 背景画像の描画
        screen.blit(bg, bg_rect)
        # プレイヤー画像の描画    
        screen.blit(player, player_rect)   
        
        screen.blit(santa, santa_rect)   
        screen.blit(santa_egao, egao_rect)   



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
                # 矢印キーなら円の中心座標を矢印の方向に移動
                if event.key == K_LEFT:
                    player_rect.centerx -= 15
                if event.key == K_RIGHT:
                    player_rect.centerx += 15
                if event.key == K_UP:
                    player_rect.centery -= 15
                if event.key == K_DOWN:
                    player_rect.centery += 15

    # Pygameとプログラムの実行を終了
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()