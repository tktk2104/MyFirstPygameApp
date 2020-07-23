from enum import Enum

# ゲームの状態
class ResultType(Enum):
    Null = -1 # 無
    Win  = 0  # 勝ち
    Lose = 1  # 負け
    Draw = 2  # 引き分け