
import pygame
from pygame.locals import *

#<
# 地面のクラス
class Ground:

    #<
    def __init__(self, screen, textureHandle):

        self.isDead         = False

        self.screen         = screen
        self.textureHandle  = textureHandle
        self.scrollTimer    = 0

        self.drawPriority   = 0
    #>


    #<
    # 自身を区別する為の名前を取得する
    def getName(self):
        return "Ground"
    #>


    #<
    def update(self):

        self.scrollTimer += 2

        if self.scrollTimer > 32:
            self.scrollTimer = 0

        i = 0   # 空の処理の関数を表したい
    #>


    #<
    def draw(self):

        for i in range(16):
            # 箱の画像を指定の座標に描画する
            self.screen.blit(self.textureHandle, (32.0 * i - self.scrollTimer, 480.0 - 32.0))
    #>
#>