import pygame
from pygame.locals import *

#<
# スコアのクラス
class Score:

    CollisionRangeWidth     = 28;
    CollisionRangeHeight    = 28;

    #<
    def __init__(self, screen, gameObjectManegr, textureHandle, scoreSound):

        self.isDead             = False

        self.screen             = screen
        self.gameObjectManegr   = gameObjectManegr
        self.textureHandle      = textureHandle
        self.scoreSound         = scoreSound

        self.curScore           = 0

        self.drawPriority       = 5
    #>


    #<
    # 自身を区別する為の名前を取得する
    def getName(self):
        return "Score"
    #>


    #<
    def update(self):

        # プレイヤーオブジェクトの取得
        playerObjects = self.gameObjectManegr.findGameObjectsWithName("Player")

        # パイプオブジェクトのリストを取得
        pipeObjects = self.gameObjectManegr.findGameObjectsWithName("EarthenPipe")

        if not playerObjects:
            return

        for gameObject in pipeObjects:

            if not gameObject.addedScore and playerObjects[0].posX > gameObject.posX:

                gameObject.addedScore = True
                self.curScore += 1
                self.scoreSound.play()
    #>

    #<
    def draw(self):

        startDrawPosX = 240 - 64 + (32 * self.countDigits(self.curScore))

        tempScore = self.curScore

        while (True):

            # 下一桁のみ取り出す
            singleDigit = tempScore % 10;

            # 画像の中のどの範囲を描画するかを指定するための値
            drawTextureU = 64 * singleDigit

            self.screen.blit(self.textureHandle, (startDrawPosX, 10), (drawTextureU, 0, 64, 64))

            # 描画位置を左へ1文字分ずらす
            startDrawPosX -= 64;

            # 数を一桁小さくする（例えば、123は12になる）
            tempScore /= 10;

            # 数が0になったら、これ以上描画するものがないので終了
            if (int(tempScore) == 0):
                break;
    #>


    #<
    # 桁数を調べる関数
    def countDigits(self, num):

        digits = 1

        while (True):

            num /= 10

            if (int(num) == 0):

                return digits

            digits += 1

        return digits
     #>
#>
