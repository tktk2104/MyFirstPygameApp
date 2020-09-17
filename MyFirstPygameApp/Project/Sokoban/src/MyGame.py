import pygame
from pygame.locals import *

from Utility.PygameWrapper.Input.KeyInput import *
from Project.Sokoban.src.GameObject.GameObjectManager   import *
from Project.Sokoban.src.GameObject.Box.Box             import *
from Project.Sokoban.src.GameObject.Goal.Goal           import *
from Project.Sokoban.src.GameObject.Player.Player       import *
from Project.Sokoban.src.GameObject.Wall.Wall           import *

#<
# 倉庫番
class MyGame:

    #<
    def __init__(self):

        # pygameの初期化
        pygame.init()

        # 変数達
        self.isGameEnd          = False                             # ゲーム終了フラグ
        self.inputGetter        = KeyInput()                        # キー入力クラス
        self.gameObjectManager  = GameObjectManager()               # ゲームオブジェクトマネージャー
        self.screen         = pygame.display.set_mode((480, 480))   # スクリーン
        self.clock          = pygame.time.Clock()                   # ウェイトタイマ

        self.wallTextureHandle   = pygame.image.load("Project/Sokoban/res/wall.png")
        self.playerTextureHandle = pygame.image.load("Project/Sokoban/res/pacchi.png")
        self.boxTextureHandle    = pygame.image.load("Project/Sokoban/res/box.png")
        self.goalTextureHandle   = pygame.image.load("Project/Sokoban/res/goal.png")
        self.clearTextureHandle   = pygame.image.load("Project/Sokoban/res/clear.png")

        # マップの読み込み
        with open('Project/Sokoban/res/Map.txt', 'r', encoding='shift_jis') as file:

            for y, line in enumerate(file):
                for x, c in enumerate(line):

                    if c == '#':
                        self.gameObjectManager.add(Wall(self.screen, self.wallTextureHandle, x, y))

                    elif c == '@':
                        self.gameObjectManager.add(Player(self.screen, self.inputGetter, self.gameObjectManager, self.playerTextureHandle, x, y))

                    elif c == '$':
                        self.gameObjectManager.add(Box(self.screen, self.boxTextureHandle, x, y))

                    elif c == '.':
                        self.gameObjectManager.add(Goal(self.screen, self.gameObjectManager, self.goalTextureHandle, x, y))

                    elif c == '+':
                        self.gameObjectManager.add(Goal(self.screen, self.gameObjectManager,  self.goalTextureHandle, x, y))
                        self.gameObjectManager.add(Player(self.screen, self.inputGetter, self.gameObjectManager, self.playerTextureHandle, x, y))
                    elif c == '+':
                        self.gameObjectManager.add(Goal(self.screen, self.gameObjectManager, self.goalTextureHandle, x, y))
                        self.gameObjectManager.add(Box(self.screen, self.boxTextureHandle, x, y))
    #>


    #->
    def __del__(self):

        # pygameの終了
        pygame.quit()
    #<


    #<
    # 更新処理
    def update(self):

        self.inputGetter.updateKey()

        if not self.gameObjectManager.isGameClear():
            self.gameObjectManager.update()
    #>


    #<
    # 描画
    def draw(self):

        self.screen.fill((0, 128, 255))

        self.gameObjectManager.draw()
    
        if self.gameObjectManager.isGameClear():
            self.screen.blit(self.clearTextureHandle, (0, 0))

        pygame.display.update()
    #>


    #<
    # ゲーム終了チェック
    def gameEndCheck(self):

        # pygameがで発生したイベントを全てチェックする
        for event in pygame.event.get():
            # ゲーム終了イベントかESCキーが入力されたら
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # ゲーム終了フラグを立てる
                self.isGameEnd = True
    #>


    #<
    # ゲームの実行
    def run(self):
        
        #----------------------------------------
        # ゲームループ
        while self.isGameEnd == False:

            # 更新処理
            self.update()

            # 描画処理
            self.draw()        
            
            # タイマウェイト
            self.clock.tick(60)

            # ゲーム終了チェック
            self.gameEndCheck()
        #----------------------------------------
    #>
#>