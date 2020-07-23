import pygame
from pygame.locals import *
import random
from enum import Enum

# ジャンケンゲーム
class Janken:
    # ゲームの状態種別
    class State(Enum):    
    	READY  = 0      # じゃんけん前
    	RESULT = 1      # じゃんけん後

    # 勝敗種別
    class Result(Enum):    
    	WIN  = 0
    	LOSE = 1
    	AIKO = 2

    # コンストラクタ
    def __init__(self):
        # 現在のゲームの状態
        self.state = Janken.State.READY
        # 勝敗を格納するための変数
        self.result = -1
        # 自分の手。1:グー, 2:チョキ, 3:パー
        self.jibun = 0
        # 相手の手
        self.aite = 0

    # ゲームの実行
    def run(self):
        # pygameの初期化
        pygame.init()
        # スクリーンの初期化
        self.screen = pygame.display.set_mode((800, 600))
        # ウェイトタイマの作成
        clock = pygame.time.Clock()
        # 開始
        self.start()
        # ゲームループ
        is_end = False
        while is_end == False:
            # 更新
            self.update(1.0)
            # 画面消去 
            self.screen.fill((0, 128, 255))
            # 描画
            self.draw()
            # 画面の更新            
            pygame.display.update()
            # タイマウェイト
            clock.tick(60)
            # 終了チェック
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    is_end = True
        # pygameの終了
        pygame.quit()

    # リソースの読み込み
    def load_content(self):
        self.texture_anata    = pygame.image.load("RockPaperScissors/res/anata.png")          # 「あなた」
        self.texture_aite     = pygame.image.load("RockPaperScissors/res/aite.png")           # 「あいて」
        self.texture_setsumei = pygame.image.load("RockPaperScissors/res/setsumei.png")       # 操作説明
        self.texture_gu       = pygame.image.load("RockPaperScissors/res/janken_gu.png")      # グーの画像
        self.texture_choki    = pygame.image.load("RockPaperScissors/res/janken_choki.png")   # チョキの画像
        self.texture_pa       = pygame.image.load("RockPaperScissors/res/janken_pa.png")      # パーの画像
        self.texture_kachi    = pygame.image.load("RockPaperScissors/res/kachi.png")          # 「勝ち！」
        self.texture_make     = pygame.image.load("RockPaperScissors/res/make.png")           # 「負け...
        self.texture_aiko     = pygame.image.load("RockPaperScissors/res/aiko.png")           # 「あいこ」  

    # 開始
    def start(self):
        # リソースの読み込み
        self.load_content()
 
    # 更新
    def update(self, game_time):
        # じゃんけん前
        if self.state == Janken.State.READY:
            input_key_push = pygame.key.get_pressed()
            self.jibun = 0
            if input_key_push[pygame.K_1] == True:
                self.jibun = 1
            elif input_key_push[pygame.K_2] == True:
                self.jibun = 2
            elif input_key_push[pygame.K_3] == True:
                self.jibun = 3      
            # ボタンが押されたか？
            if self.jibun != 0:
                # 相手の手を決める
                self.aite = random.randrange(1, 4)
                # 勝敗を判定する
                if self.jibun == self.aite:
                    # あいこ
                    self.result = Janken.Result.AIKO
                # 1行の式を複数行に分ける場合は\でつなげる(日本語フォントだと半角の￥マーク）
                elif (self.jibun == 1 and self.aite == 2) \
                  or (self.jibun == 2 and self.aite == 3) \
                  or (self.jibun == 3 and self.aite == 1):
                    # 勝ち
                    self.result = Janken.Result.WIN
                else:
                    # 負け
                    self.result = Janken.Result.LOSE
                self.state = Janken.State.RESULT
        elif self.state == Janken.State.RESULT:
            return # 何もしない


    # 描画
    def draw(self):
        #「あいて」の描画
        self.screen.blit(self.texture_aite, (20, 20))
        # 「あなた」の描画
        self.screen.blit(self.texture_anata, (20, 210))
        # じゃんけん前の描画処理
        if self.state == Janken.State.READY:
            # 操作説明の描画
            self.screen.blit(self.texture_setsumei, (330, 160))
        # じゃんけん後の描画処理
        elif self.state == Janken.State.RESULT:
            # あいての手の描画
            self.screen.blit(self.get_te_texture(self.aite), (330, 20))
            # 自分の手の描画
            self.screen.blit(self.get_te_texture(self.jibun), (330, 210))
            # 結果の描画
            if self.result == Janken.Result.WIN:
                result_texture = self.texture_kachi
            elif self.result == Janken.Result.LOSE:
                result_texture = self.texture_make
            else:
                result_texture = self.texture_aiko
            self.screen.blit(result_texture, (480, 210))

    # 手の番号をテクスチャに変換
    def get_te_texture(self, te):
        if te == 1: return self.texture_gu    
        if te == 2: return self.texture_choki 
        if te == 3: return self.texture_pa    

# じゃんけんゲームの実行
Janken().run()