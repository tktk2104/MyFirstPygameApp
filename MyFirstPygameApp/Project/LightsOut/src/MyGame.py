import pygame
from pygame.locals import *
import random

from Utility.Math.Vector2 import *
from Utility.PygameWrapper.Input.MouseInput import *
from Project.LightsOut.src.GameLogic.ResourceLoader import *

#->
# ライツアウト
class MyGame:

    #->
    def __init__(self):

        # pygameの初期化
        pygame.init()

        # 変数達
        self.isGameEnd      = False             # ゲーム終了フラグ
        self.isGamePlaying  = True              # ゲームプレイフラグ
        self.bordSize       = 5                 # ボードの大きさ
        self.boardData      = []                # ボードの状態
        self.resourceLoader = ResourceLoader()  # リソース読み込み、管理クラス
        self.inputGetter    = MouseInput()      # マウス入力取得クラス
        self.boardOrigin    = Vector2(100, 100) # ボードの中心点（ピクセル）
        self.gridSize       = 64                # グリッドの大きさ（ピクセル）

        self.screen         = pygame.display.set_mode((800, 600))   # スクリーン
        self.clock          = pygame.time.Clock()                   # ウェイトタイマ

        # ボードの情報を初期化
        for i in range(self.bordSize):
            self.boardData.append([False] * self.bordSize)
            for j in range(self.bordSize):
                self.boardData[i][j] = (random.randrange(0, 2) == 0)
    #<


    #->
    def __del__(self):

        # pygameの終了
        pygame.quit()
    #<


    #->
    # プレイヤーの入力
    def playerInput(self):

        # マウスの座標を取得
        mousePos = self.inputGetter.getPosition()
        
        # マウス座標がボードの外を指していたら座標取得失敗
        if (mousePos.x < self.boardOrigin.x or mousePos.y < self.boardOrigin.y or mousePos.x > self.boardOrigin.x + self.bordSize * self.gridSize or mousePos.y > self.boardOrigin.y + self.bordSize * self.gridSize):
            return (False, (0, 0))

        # マウス座標をボード座標に変換する
        boardPos = (int((mousePos.x - self.boardOrigin.x) / self.gridSize), int((mousePos.y - self.boardOrigin.y) / self.gridSize));

        # 座標取得成功
        return (True, boardPos)
    #<


    #->
    def pushButton(self, position):

        if position[0] < 0 or position[1] < 0 or position[0] >= self.bordSize or position[1] >= self.bordSize:
            return

        self.boardData[position[1]][position[0]] = not self.boardData[position[1]][position[0]]
    #<


    #->
    # プレイヤーの入力
    def updateBoard(self, position):

        self.pushButton(position)
        self.pushButton((position[0] + 1, position[1]))
        self.pushButton((position[0] - 1, position[1]))
        self.pushButton((position[0], position[1] + 1))
        self.pushButton((position[0], position[1] - 1))

        # ボードが１つでも点灯していたら関数を終わる
        for y in range(self.bordSize):
             for x in range(self.bordSize):
                 if self.boardData[y][x]:
                     return

        # ゲームを終了する
        self.isGamePlaying = False
    #<

 
    #->
    # 更新処理
    def update(self):

        # 入力の更新処理
        self.inputGetter.updateMouse();

        if self.isGamePlaying:

            # チートコード
            if self.inputGetter.isTrigger(MouseButtonType.Center):
                for y in range(self.bordSize):
                     for x in range(self.bordSize):
                         self.boardData[y][x] = False

            # 左クリックが押されたら
            if self.inputGetter.isTrigger(MouseButtonType.Left):

                # 入力座標（ボード座標）
                inputPos = self.playerInput()

                # 座標取得に失敗した場合は何もしない
                if not inputPos[0]:
                    return

                # 盤面を更新する
                self.updateBoard(inputPos[1])
    #<


    #->
    # スプライト描画関数（Vector2で座標指定版）
    def drawSprite(self, texture, position):
        self.screen.blit(texture, (position.x, position.y))
    #<


    #->
    # 描画
    def draw(self):

        self.screen.fill((0, 128, 255))

        #----------------------------------------
        # ボード状況を描画
        for y, lineData in enumerate(self.boardData):

            #------------------------------
            # 列ごとにループ
            for x, boxData in enumerate(lineData):

                if boxData:
                    self.drawSprite(self.resourceLoader.texture_button_on, self.boardOrigin + Vector2(self.gridSize * x, self.gridSize * y))
                else:
                    self.drawSprite(self.resourceLoader.texture_button_off, self.boardOrigin + Vector2(self.gridSize * x, self.gridSize * y))
            #------------------------------
        #----------------------------------------

        if self.isGamePlaying:
            self.drawSprite(self.resourceLoader.texture_order, Vector2(0.0, 0.0))
        else:
            self.drawSprite(self.resourceLoader.texture_gameclear, Vector2(0.0, 0.0))
    
        pygame.display.update()
    #<


    #->
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
    #<


    #->
    # ゲーム終了チェック
    def gameEndCheck(self):

        # pygameがで発生したイベントを全てチェックする
        for event in pygame.event.get():
            # ゲーム終了イベントかESCキーが入力されたら
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # ゲーム終了フラグを立てる
                self.isGameEnd = True
    #<
#<