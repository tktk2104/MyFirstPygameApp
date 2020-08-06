import pygame
from pygame.locals import *

class ResourceLoader:
    def __init__(self):
        # リソースのハンドル達
        self.texture_maru           = pygame.image.load("Project/TicTacToe/res/maru.png")         # 「まる」
        self.texture_batsu          = pygame.image.load("Project/TicTacToe/res/batsu.png")        # 「ばつ」
        self.texture_grid           = pygame.image.load("Project/TicTacToe/res/grid.png")         # ステージの外枠
        self.texture_nobandesu      = pygame.image.load("Project/TicTacToe/res/nobandesu.png")    # 手番を表示するUI
        self.texture_nokachidesu    = pygame.image.load("Project/TicTacToe/res/nokachidesu.png")  # 「勝ち！」
        self.texture_hikiwake       = pygame.image.load("Project/TicTacToe/res/hikiwake.png")     # 「引き分け」