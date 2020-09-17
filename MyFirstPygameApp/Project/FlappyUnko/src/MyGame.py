import pygame
from pygame.locals import *
import random

from Utility.PygameWrapper.Input.KeyInput                       import *
from Project.FlappyUnko.src.GameObject.GameObjectManager        import *
from Project.FlappyUnko.src.GameObject.Ground.Ground            import *
from Project.FlappyUnko.src.GameObject.Player.Player            import *
from Project.FlappyUnko.src.GameObject.EarthenPipe.EarthenPipe  import *
from Project.FlappyUnko.src.GameObject.Score.Score              import *
from Project.FlappyUnko.src.Enum.GameState                      import *

#<
# フラッピーうんこ
class MyGame:

    #<
    def __init__(self):

        # pygameの初期化
        pygame.init()

        # mixerモジュールの初期化
        pygame.mixer.init()

        # 変数達
        self.isGameEnd          = False                             # ゲーム終了フラグ
        self.inputGetter        = KeyInput()                        # キー入力クラス
        self.gameObjectManager  = GameObjectManager()               # ゲームオブジェクトマネージャー
        self.screen         = pygame.display.set_mode((480, 480))   # スクリーン
        self.clock          = pygame.time.Clock()                   # ウェイトタイマ
        
        self.curState       = GameState.Title                       # 現在のゲームの状態

        # 画像の読み込み
        self.dokan_bodyTextureHandle    = pygame.image.load("Project/FlappyUnko/res/dokan_body.png")
        self.dokan_endTextureHandle     = pygame.image.load("Project/FlappyUnko/res/dokan_end.png")
        self.floorTextureHandle         = pygame.image.load("Project/FlappyUnko/res/floor.png")
        self.gameoverTextureHandle      = pygame.image.load("Project/FlappyUnko/res/gameover.png")
        self.numbersTextureHandle       = pygame.image.load("Project/FlappyUnko/res/numbers.png")
        self.startGuideTextureHandle    = pygame.image.load("Project/FlappyUnko/res/push_space_to_start.png")
        self.titleTextureHandle         = pygame.image.load("Project/FlappyUnko/res/title.png")
        self.unkoTextureHandle          = pygame.image.load("Project/FlappyUnko/res/unko.png")

        # サウンドの読み込み
        self.soundJump      = pygame.mixer.Sound("Project/FlappyUnko/res/se_jump.wav")
        self.soundScore     = pygame.mixer.Sound("Project/FlappyUnko/res/se_coin.wav")
        self.soundDamage    = pygame.mixer.Sound("Project/FlappyUnko/res/se_noise.wav")

        self.flashTimer = 0
        self.spawnTimer = 120

        # 初期オブジェクトの作成
        self.gameObjectManager.add(Ground(self.screen, self.floorTextureHandle))
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
        self.gameObjectManager.update()

        self.flashTimer += 1

        if self.flashTimer > 60:
            self.flashTimer = 0

        if self.curState == GameState.Title:

            if self.inputGetter.isTrigger(K_SPACE):

                self.gameObjectManager.add(Score(self.screen, self.gameObjectManager, self.numbersTextureHandle, self.soundScore))
                self.gameObjectManager.add(Player(self.screen, self.inputGetter, self.gameObjectManager, self.unkoTextureHandle, self.soundJump, self.soundDamage, 100, 200))
                self.curState = GameState.GamePlay

        elif self.curState == GameState.GamePlay:

            self.spawnTimer += 1

            if self.spawnTimer > 120:
                self.gameObjectManager.add(EarthenPipe(self.screen, self.dokan_endTextureHandle, self.dokan_bodyTextureHandle, random.randrange(-60, 60), 480))
                self.spawnTimer = 0

            if self.gameObjectManager.isGameOver():

                self.curState = GameState.GameOver
    #>


    #<
    # 描画
    def draw(self):

        self.screen.fill((0, 128, 255))

        self.gameObjectManager.draw()

        if self.curState == GameState.Title:

            self.screen.blit(self.titleTextureHandle, (123, 100))

            if self.flashTimer > 30:
                self.screen.blit(self.startGuideTextureHandle, (40, 300))

        elif self.curState == GameState.GameOver:
            self.screen.blit(self.gameoverTextureHandle, (144, 200))

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