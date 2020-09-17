import pygame
from pygame.locals import *

#<
# プレイヤーのクラス
class Player:

    CollisionRangeWidth     = 28;
    CollisionRangeHeight    = 28;

    #<
    def __init__(self, screen, inputGetter, gameObjectManegr, textureHandle, jumpSound, damageSound, posX, posY):

        self.isDead             = False

        self.screen             = screen
        self.inputGetter        = inputGetter
        self.gameObjectManegr   = gameObjectManegr
        self.textureHandle      = textureHandle
        self.jumpSound          = jumpSound
        self.damageSound        = damageSound
        self.posX               = posX
        self.posY               = posY
        self.verticalVelocity   = 0
        self.drawPriority       = 2
    #>


    #<
    # 自身を区別する為の名前を取得する
    def getName(self):
        return "Player"
    #>


    #<
    def update(self):

        self.posY -= self.verticalVelocity

        self.verticalVelocity -= 1

        if self.inputGetter.isTrigger(K_SPACE):
            self.jumpSound.play()
            self.verticalVelocity = 10

        if self.posY < 0 or self.posY > 480:
            self.damageSound.play()
            self.isDead = True

        # パイプオブジェクトのリストを取得
        pipeObjects = self.gameObjectManegr.findGameObjectsWithName("EarthenPipe")

        for gameObject in pipeObjects:

            # 上の土管の中心点
            upDokanCenterPosX = gameObject.posX + 32
            upDokanCenterPosY = gameObject.upDokanTop / 2
            
            # 自身と上の土管の中心点の差
            upDokanDistX = self.posX - upDokanCenterPosX
            upDokanDistY = self.posY - upDokanCenterPosY
            
            if (abs(upDokanDistX) < 32 + Player.CollisionRangeWidth / 2) and (abs(upDokanDistY) < gameObject.upDokanTop / 2 + Player.CollisionRangeHeight / 2):
                self.damageSound.play()
                self.isDead = True
                return

            # 下の土管の中心点
            downDokanCenterPosX = gameObject.posX + 32
            downDokanCenterPosY = gameObject.downDokanTop + (480 - gameObject.downDokanTop) / 2

            # 自身と下の土管の中心点の差
            downDokanDistX = self.posX - downDokanCenterPosX
            downDokanDistY = self.posY - downDokanCenterPosY

            if (abs(downDokanDistX) < 32 + Player.CollisionRangeWidth / 2) and (abs(downDokanDistY) < (480 - gameObject.downDokanTop) / 2 + Player.CollisionRangeHeight / 2):
                self.damageSound.play()
                self.isDead = True
    #>

    #<
    def draw(self):

        # プレイヤーの画像を指定の座標に描画する
        self.screen.blit(self.textureHandle, (self.posX - 48, self.posY - 48))
    #>
#>