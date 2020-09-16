
import pygame
from pygame.locals import *

#<
# ゴールのクラス
class Goal:

    #<
    def __init__(self, screen, gameObjectManegr, textureHandle, posX, posY):

        self.screen             = screen
        self.gameObjectManegr   = gameObjectManegr
        self.textureHandle      = textureHandle
        self.posX               = posX
        self.posY               = posY
        self.onBox              = False
    #>


    #<
    # 自身を区別する為の名前を取得する
    def getName(self):
        return "Goal"
    #>


    #<
    # マス目座標（int, int）を取得する
    def getGridPos(self):

        return (self.posX, self.posY)
    #>


    #<
    def update(self):

        self.onBox = False

        onObjects = self.gameObjectManegr.findGameObjectsWithGridPos(self.posX, self.posY)

        for gameObject in onObjects:

            if gameObject.getName() == "Box":
                self.onBox = True
    #>


    #<
    def draw(self):

        # ゴールの画像を指定の座標に描画する
        self.screen.blit(self.textureHandle, (self.posX * 32.0, self.posY * 32.0))
    #>
#>