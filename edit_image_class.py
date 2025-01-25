import sys
import pygame
from pygame.locals import *
class edit_image:
    def resize(self,orig,new_width):
        orig_x = orig.get_width()
        orig_y = orig.get_height()

        result = pygame.transform.smoothscale(orig,(new_width,orig_y*(new_width/orig_x)))
        return result

def main():
    SCREEN_WIDTH = 1600/2
    SCREEN_HEIGHT = 900/2
        # Pygameの初期化
    pygame.init()
    # 画面設定
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    screen = pygame.display.get_surface()
    santa = pygame.image.load("image/magao.png").convert_alpha()
    santa = edit_image().resize(santa,100)
    santa_rect = santa.get_rect()



    #サンタ画像の初期位置
    santa_rect.center = (300,300) 

    running = True  # ループ処理の実行を継続するフラグ

    while running:
        # 画面更新
        pygame.display.update()  
        # 更新間隔（30msec）           
        pygame.time.wait(30)
        # 画面の背景色（RGBA）     
        screen.fill((100, 0, 0, 0))
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
            
    # Pygameとプログラムの実行を終了
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()