import pygame

class ResourceLoader:
    def __init__(self):
        # リソースのハンドル達
        self.texture_anata    = pygame.image.load("Project/RockPaperScissors/res/anata.png")        # 「あなた」
        self.texture_aite     = pygame.image.load("Project/RockPaperScissors/res/aite.png")         # 「あいて」
        self.texture_setsumei = pygame.image.load("Project/RockPaperScissors/res/setsumei.png")     # 操作説明
        self.texture_gu       = pygame.image.load("Project/RockPaperScissors/res/janken_gu.png")    # グーの画像
        self.texture_choki    = pygame.image.load("Project/RockPaperScissors/res/janken_choki.png") # チョキの画像
        self.texture_pa       = pygame.image.load("Project/RockPaperScissors/res/janken_pa.png")    # パーの画像
        self.texture_kachi    = pygame.image.load("Project/RockPaperScissors/res/kachi.png")        # 「勝ち！」
        self.texture_make     = pygame.image.load("Project/RockPaperScissors/res/make.png")         # 「負け...
        self.texture_aiko     = pygame.image.load("Project/RockPaperScissors/res/aiko.png")         # 「あいこ」