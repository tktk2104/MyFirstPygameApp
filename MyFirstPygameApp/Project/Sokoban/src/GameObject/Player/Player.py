import pygame
from pygame.locals import *

#<
# プレイヤーのクラス
class Player:

    #<
    def __init__(self, screen, inputGetter, gameObjectManegr, textureHandle, posX, posY):

        self.screen             = screen
        self.inputGetter        = inputGetter
        self.gameObjectManegr   = gameObjectManegr
        self.textureHandle      = textureHandle
        self.posX               = posX
        self.posY               = posY
        self.inputIntervalTimer = 0
    #>


    #<
    # 自身を区別する為の名前を取得する
    def getName(self):
        return "Player"
    #>


    #<
    # マス目座標（int, int）を取得する
    def getGridPos(self):

        return (self.posX, self.posY)
    #>


    #<
    def update(self):

        if self.inputIntervalTimer > 0:
            self.inputIntervalTimer -= 1
            return

        if self.inputGetter.isPush(K_UP):
            self.move( 0, -1)

        if self.inputGetter.isPush(K_DOWN):
            self.move( 0,  1)

        if self.inputGetter.isPush(K_LEFT):
            self.move(-1,  0)

        if self.inputGetter.isPush(K_RIGHT):
            self.move( 1,  0)
    #>


    #<
    def move(self, x, y):

        # 仮の移動先座標を計算
        tempMovePosX = self.posX + x
        tempMovePosY = self.posY + y

        movePosObjects = self.gameObjectManegr.findGameObjectsWithGridPos(tempMovePosX, tempMovePosY)

        for gameObject in movePosObjects:

            if gameObject.getName() == "Wall":
                return

            if gameObject.getName() == "Box":
                if not self.moveBox(gameObject, tempMovePosX + x, tempMovePosY + y):
                    return
                
        self.posX = tempMovePosX
        self.posY = tempMovePosY
        self.inputIntervalTimer = 10
    #>


    #<
    def moveBox(self, boxObject, tempBoxMovePosX, tempBoxMovePosY):

        movePosObjects = self.gameObjectManegr.findGameObjectsWithGridPos(tempBoxMovePosX, tempBoxMovePosY)

        for gameobject in movePosObjects:

            if gameobject.getName() == "Wall" or gameobject.getName() == "Box":
                return False

        boxObject.posX = tempBoxMovePosX
        boxObject.posY = tempBoxMovePosY

        return True
    #>


    #<
    def draw(self):

        # プレイヤーの画像を指定の座標に描画する
        self.screen.blit(self.textureHandle, (self.posX * 32.0, self.posY * 32.0))
    #>
#>