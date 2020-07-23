import pygame
from pygame.locals import *
import random

from RockPaperScissors.src.Enum.GameState import *
from RockPaperScissors.src.Enum.ResultType import *
from RockPaperScissors.src.Enum.RpsPlan import *
from RockPaperScissors.src.GameLogic.ResourceLoader import *
from RockPaperScissors.src.GameLogic.KeyInput import *

# ジャンケンゲーム
class MyGame:

    #<
    def __init__(self):

        # pygameの初期化
        pygame.init()

        # 変数達
        self.isGameEnd      = False                                 # ゲーム終了フラグ
        self.state          = GameState.Ready                       # 現在のゲームの状態
        self.result         = ResultType.Null                       # 勝敗
        self.playerPlan     = RpsPlan.Null                          # プレイヤーの手
        self.enemyPlan      = RpsPlan.Null                          # 敵の手
        self.resourceLoader = ResourceLoader()                      # リソース読み込み、管理クラス
        self.inputGetter    = KeyInput()                            # キー入力取得クラス
        self.screen         = pygame.display.set_mode((800, 600))   # スクリーン
        self.clock          = pygame.time.Clock()                   # ウェイトタイマ
    #>


    #<
    def __del__(self):

        # pygameの終了
        pygame.quit()
    #>


    #<
    # ゲームの実行
    def run(self):
        
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
    # 更新処理
    def update(self):

        # 入力の更新処理
        self.inputGetter.updateKey();
        
        # 今がプレイヤー入力待ち状態だったら
        if self.state == GameState.Ready:
            
            # プレイヤーの入力を取得する
            self.getPlayerInput()

            # プレイヤーの入力がされていたら
            if self.playerPlan != RpsPlan.Null:

                # 入力されたキーの情報を取得
                inputKeyPushData = pygame.key.get_pressed()

                # スペースキーが入力された場合
                if self.inputGetter.isTrigger(pygame.K_SPACE):

                    # 敵の手を決める
                    self.setEnemyPlan()

                    # 勝敗を判定する
                    self.WinLossJudge()

                    # 勝敗結果状態にする
                    self.state = GameState.Result

        # 今が勝敗結果状態だったら
        elif self.state == GameState.Result:
            
            # スペースキーが入力された場合、ゲームをリセットする
            if self.inputGetter.isTrigger(pygame.K_SPACE):
                self.state      = GameState.Ready
                self.result     = ResultType.Null
                self.playerPlan = RpsPlan.Null
                self.enemyPlan  = RpsPlan.Null
    #>


    #<
    # プレイヤーの入力を取得する
    def getPlayerInput(self):

        # キー入力に対応したプレイヤーの手に変更する
        if self.inputGetter.isTrigger(pygame.K_1):
            self.playerPlan = RpsPlan.Rock
        elif self.inputGetter.isTrigger(pygame.K_2):
            self.playerPlan = RpsPlan.Scissors
        elif self.inputGetter.isTrigger(pygame.K_3):
            self.playerPlan = RpsPlan.Paper      
    #>


    #<
    # 敵の手を決める
    def setEnemyPlan(self):
        self.enemyPlan = RpsPlan(random.randrange(1, 4))
    #>


    #<
    # 勝敗を判定する
    def WinLossJudge(self):

        # 勝敗判定に使用する数字
        JudgeNum = (self.playerPlan - self.enemyPlan + 3) % 3

        # 0だったらあいこ
        if JudgeNum == 0:
            self.result = ResultType.Draw

        # 1だったら負け
        elif JudgeNum == 1:
            self.result = ResultType.Lose

        # 2だったら勝ち
        elif JudgeNum == 2:
            self.result = ResultType.Win
    #>


    #<
    # 描画
    def draw(self):

        self.screen.fill((0, 128, 255))

        #「あいて」の描画
        self.screen.blit(self.resourceLoader.texture_aite, (20, 20))

        # 「あなた」の描画
        self.screen.blit(self.resourceLoader.texture_anata, (20, 210))

        if self.playerPlan != RpsPlan.Null:

            # 自分の手の描画
            self.screen.blit(self.getRpsPlanTexture(self.playerPlan), (330, 210))

        # じゃんけん前の描画処理
        if self.state == GameState.Ready:

            # あいてが手を選んでいる様子の描画
            self.screen.blit(self.getRpsPlanTexture(RpsPlan(random.randrange(1, 4))), (330, 20))

            # 操作説明の描画
            self.screen.blit(self.resourceLoader.texture_setsumei, (100, 330))

        # じゃんけん後の描画処理
        elif self.state == GameState.Result:

            # あいての手の描画
            self.screen.blit(self.getRpsPlanTexture(self.enemyPlan), (330, 20))

            # 結果の描画
            if self.result == ResultType.Win:
                resultTexture = self.resourceLoader.texture_kachi

            elif self.result == ResultType.Lose:
                resultTexture = self.resourceLoader.texture_make

            else:
                resultTexture = self.resourceLoader.texture_aiko

            self.screen.blit(resultTexture, (480, 210))

        pygame.display.update()
    #>

    # 手の番号をテクスチャに変換
    def getRpsPlanTexture(self, plan):
        if plan == RpsPlan.Rock:      return self.resourceLoader.texture_gu    
        if plan == RpsPlan.Scissors:  return self.resourceLoader.texture_choki 
        if plan == RpsPlan.Paper:     return self.resourceLoader.texture_pa