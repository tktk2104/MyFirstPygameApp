# 列挙型をインポート
from enum import Enum

class GameState(Enum):
    Playing           = 1   # プレイ中
    PlayerOneWin      = 2   # oの勝ち
    PlayerTwoWin      = 3   # xの勝ち
    Draw              = 4   # 引き分け