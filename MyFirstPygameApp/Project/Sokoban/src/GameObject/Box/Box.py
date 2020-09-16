
import pygame
from pygame.locals import *

#<
# 箱のクラス
class Box:

    #<
    def __init__(self, screen, textureHandle, posX, posY):

        self.screen         = screen
        self.textureHandle  = textureHandle
        self.posX           = posX
        self.posY           = posY
    #>


    #<
    # 自身を区別する為の名前を取得する
    def getName(self):
        return "Box"
    #>


    #<
    # マス目座標（int, int）を取得する
    def getGridPos(self):

        return (self.posX, self.posY)
    #>


    #<
    def update(self):

        i = 0   # 空の処理の関数を表したい
    #>


    #<
    def draw(self):

        # 箱の画像を指定の座標に描画する
        self.screen.blit(self.textureHandle, (self.posX * 32.0, self.posY * 32.0))
    #>
#>