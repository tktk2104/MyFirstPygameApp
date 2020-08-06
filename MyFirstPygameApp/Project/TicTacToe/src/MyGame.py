import pygame
from pygame.locals import *

from Utility.Math.Vector2 import *
from Project.TicTacToe.src.Enum.GameState import *
from Project.TicTacToe.src.GameLogic.ResourceLoader import *
from Utility.PygameWrapper.Input.MouseInput import *

#->
# ゲームクラス
class TicTacToe:
  
    #->
    # コンストラクタ
    def __init__(self, bordSize):

        # pygameの初期化
        pygame.init()
    
        # メンバ変数の定義
        self.isGameEnd      = False                                 # ゲーム終了フラグ
        self.state          = GameState.Playing                     # 現在のゲームの状態
        self.resourceLoader = ResourceLoader()                      # リソース読み込み、管理クラス
        self.inputGetter    = MouseInput()                          # マウス入力取得クラス
        self.screen         = pygame.display.set_mode((800, 600))   # スクリーン
        self.clock          = pygame.time.Clock()                   # ウェイトタイマ
        self.bordSize       = bordSize                              # ボードの大きさ
        self.boardData      = []                                    # ボードの情報
        self.turnPlayer     = 1                                     # ターンプレイヤー
        self.turnCount      = 1                                     # ターンの経過数
        self.boardOrigin    = Vector2(100, 100)                     # ボードの中心点（ピクセル）
        self.gridSize       = 64                                    # グリッドの大きさ（ピクセル）

        # ボードの情報を初期化
        for i in range(bordSize):
            self.boardData.append([0] * bordSize)
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

        # ボード座標のマスが既にどちらかのプレイヤーの所有物だったら座標取得失敗
        if self.boardData[boardPos[1]][boardPos[0]] != 0:
            return (False, (0, 0))

        # 座標取得成功
        return (True, boardPos)
    #<

    #->
    # 指定のマス目から指定の方向に指定の個数の同じマークが繋がっているかチェックする
    def boxCheck(self, x, y, dirX, dirY, count):

        # 値がコピーされていない想定
        curX = x
        curY = y

        # 判定するマークの種類（初期値は判定を始めるマス目のマーク）
        judgeMark = self.boardData[y][x]

        # 空欄マスで判定しようとしたら強制失敗
        if judgeMark == 0:
            return False

        #----------------------------------------
        # 最初のマス目以外のマークを判定
        for i in range(count - 1):

            # 判定するマス目の位置を更新
            curX += dirX
            curY += dirY

            # マス目がボードの外を指していたら強制失敗
            if curY < 0 or curY >= len(self.boardData) or curX < 0 or curX >= len(self.boardData[curY]):
                return False

            # 判定するマークと違ったら失敗
            if self.boardData[curY][curX] != judgeMark:
                return False
        #----------------------------------------

        # ここまで実行できたという事はマークが連続している証拠

        # マークがプレイヤー１だったらプレイヤー１の勝ち
        if judgeMark == 1:
            self.state = GameState.PlayerOneWin
            return True

        # マークがプレイヤー２だったらプレイヤー２の勝ち
        elif judgeMark == 2:
            self.state = GameState.PlayerTwoWin
            return True

        #ここに来たら大問題
        print("error")
        return False
    #<


    #->
    # ボードの状態をチェックする
    def boardCheck(self):
        for y in range(self.bordSize):
            for x in range(self.bordSize):
                if self.boxCheck(x, y, 1, 0, self.bordSize) or self.boxCheck(x, y, 0, 1, self.bordSize) or self.boxCheck(x, y, 1, 1, self.bordSize) or self.boxCheck(x, y, 1, -1, self.bordSize):
                    break
    #<


    #->
    # 更新処理
    def update(self):

        # 入力の更新処理
        self.inputGetter.updateMouse();

        # プレイ中だったら
        if self.state == GameState.Playing:

            # 左クリックが押されたら
            if self.inputGetter.isTrigger(MouseButtonType.Left):

                # 入力座標（ボード座標）
                inputPos = self.playerInput()

                # 座標取得に失敗した場合は何もしない
                if not inputPos[0]:
                    return
        
                # 値を更新する
                self.boardData[inputPos[1][1]][inputPos[1][0]] = self.turnPlayer
        
                # 判定
                self.boardCheck()
        
                if self.state == GameState.Playing and self.turnCount == (self.bordSize * self.bordSize):
                    self.state = GameState.Draw
                    return
        
                # ターンを１進める
                self.turnCount += 1
        
                # ターンプレイヤーを変更する
                self.turnPlayer += 1
        
                if self.turnPlayer > 2:
                    self.turnPlayer = 1
    #<


    #->
    # スプライト描画関数（Vector2で座標指定版）
    def drawSprite(self, texture, position):
        self.screen.blit(texture, (position.x, position.y))
    #<


    #->
    # 描画処理
    def draw(self):

        self.screen.fill((0, 128, 255))

        #----------------------------------------
        # ボード状況を描画
        for y, lineData in enumerate(self.boardData):

            #------------------------------
            # 列ごとにループ
            for x, boxData in enumerate(lineData):

                # マス毎に描画
                self.drawSprite(self.resourceLoader.texture_grid, self.boardOrigin + Vector2(self.gridSize * x, self.gridSize * y))

                if boxData == 1:
                    self.drawSprite(self.resourceLoader.texture_maru, self.boardOrigin + Vector2(self.gridSize * x, self.gridSize * y))
                elif boxData == 2:
                    self.drawSprite(self.resourceLoader.texture_batsu, self.boardOrigin + Vector2(self.gridSize * x, self.gridSize * y))
            #------------------------------
        #----------------------------------------

        # 各状態毎のUI表示
        if self.state == GameState.Playing:

            if self.turnPlayer == 1:
                self.drawSprite(self.resourceLoader.texture_maru, Vector2(0, 0))
            elif self.turnPlayer == 2:
                self.drawSprite(self.resourceLoader.texture_batsu, Vector2(0, 0))

            self.drawSprite(self.resourceLoader.texture_nobandesu, Vector2(64, 0))

        elif self.state == GameState.PlayerOneWin:

            self.drawSprite(self.resourceLoader.texture_maru, Vector2(0, 0))
            self.drawSprite(self.resourceLoader.texture_nokachidesu, Vector2(64, 0))

        elif self.state == GameState.PlayerTwoWin:

            self.drawSprite(self.resourceLoader.texture_batsu, Vector2(0, 0))
            self.drawSprite(self.resourceLoader.texture_nokachidesu, Vector2(64, 0))

        elif self.state == GameState.Draw:

            self.drawSprite(self.resourceLoader.texture_hikiwake, Vector2(64, 0))

        pygame.display.update()
    #<


    #->
    # 実行関数
    def run(self):

        #----------------------------------------
        # ゲームが続いている限りループ
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