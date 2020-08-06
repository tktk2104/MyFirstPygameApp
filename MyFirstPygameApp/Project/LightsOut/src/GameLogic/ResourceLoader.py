import pygame
from pygame.locals import *

class ResourceLoader:
    def __init__(self):
        # リソースのハンドル達
        self.texture_button_off = pygame.image.load("Project/LightsOut/res/button_off.png") # 消灯
        self.texture_button_on  = pygame.image.load("Project/LightsOut/res/button_on.png")  # 点灯
        self.texture_gameclear  = pygame.image.load("Project/LightsOut/res/gameclear.png")  # ゲームクリア
        self.texture_order      = pygame.image.load("Project/LightsOut/res/order.png")      # ゲームクリア条件を示すUI