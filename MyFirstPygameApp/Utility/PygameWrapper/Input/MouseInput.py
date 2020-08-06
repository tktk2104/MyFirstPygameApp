import pygame
from pygame.locals import *

from Utility.Math.Vector2 import *
from Utility.PygameWrapper.Input.MouseButtonType import *

# マウス入力取得クラス
class MouseInput:
    def __init__(self):
        self.curInputData = pygame.mouse.get_pressed()
        self.preInputData = pygame.mouse.get_pressed()

    # マウス情報の更新
    def updateMouse(self):
        self.preInputData = self.curInputData
        self.curInputData = pygame.mouse.get_pressed()

    # 引数のマウスボタンが押されているか？
    def isPush(self, mouseBtnType):
        return self.curInputData[mouseBtnType]

     # 引数のマウスボタンが押され始めたか？
    def isTrigger(self, mouseBtnType):
        return self.curInputData[mouseBtnType] and not self.preInputData[mouseBtnType]

    # マウスポインタの座標を取得する
    def getPosition(self):
        pos = pygame.mouse.get_pos()
        return Vector2(pos[0], pos[1])