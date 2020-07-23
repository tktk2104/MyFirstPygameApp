from enum import IntEnum

# 出せる手の種類
class RpsPlan(IntEnum):
    Null        = 0 # 無
    Rock        = 1 # グー
    Scissors    = 2 # チョキ
    Paper       = 3 # パー