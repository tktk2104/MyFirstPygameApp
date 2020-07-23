from enum import Enum

# ゲームの状態
class GameState(Enum):
    Ready   = 0 # プレイヤー入力待ち状態
    Result  = 1 # 勝敗結果状態
