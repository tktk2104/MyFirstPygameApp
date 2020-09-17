import pygame
from pygame.locals import *

#<
# 上下セットのパイプのクラス
class EarthenPipe:

    # 土管の上下の隙間の広さ
    DokanVerticalSpace = 150

    # ステージのｙ軸での中心座標
    StageCenterY = (480 - 32) / 2

    #<
    def __init__(self, screen, pipeHeadTextureHandle, pipeBodyTextureHandle, offsetFromCenter, posX):

        self.isDead                     = False

        self.screen                     = screen
        self.pipeHeadTextureHandle      = pipeHeadTextureHandle

        self.upDokanTop                 = EarthenPipe.StageCenterY - EarthenPipe.DokanVerticalSpace / 2 + offsetFromCenter
        self.downDokanTop               = self.upDokanTop + EarthenPipe.DokanVerticalSpace;

        self.pipeUpBodyTextureHandle    = pygame.transform.scale(pipeBodyTextureHandle, (64, int(self.upDokanTop)))
        self.pipeDownBodyTextureHandle  = pygame.transform.scale(pipeBodyTextureHandle, (64, int(EarthenPipe.StageCenterY - EarthenPipe.DokanVerticalSpace / 2 - offsetFromCenter)))

        self.posX                       = posX
        self.addedScore                 = False

        self.drawPriority               = 3
    #>


    #<
    # 自身を区別する為の名前を取得する
    def getName(self):
        return "EarthenPipe"
    #>


    #<
    def update(self):

        self.posX -= 2

        if self.posX < -64:
            self.isDead = True
    #>


    #<
    def draw(self):

        # 上側の土管の描画
        self.screen.blit(self.pipeUpBodyTextureHandle,      (self.posX, 0))
        self.screen.blit(self.pipeHeadTextureHandle,        (self.posX, self.upDokanTop))

        # 下側の土管の描画
        self.screen.blit(self.pipeDownBodyTextureHandle,    (self.posX, self.downDokanTop))
        self.screen.blit(self.pipeHeadTextureHandle,        (self.posX, self.downDokanTop))
    #>
#>