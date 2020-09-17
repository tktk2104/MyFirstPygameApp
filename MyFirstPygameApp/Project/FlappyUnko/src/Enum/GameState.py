from enum import Enum

# ゲームの状態
class GameState(Enum):
    Title       = 0 # タイトル
    GamePlay    = 1 # ゲーム中
    GameOver    = 2 # ゲームオーバー
