from Math.Vector2 import * # Vector2クラスのインポート

a = Vector2(1, 2)
b = Vector2(2, 3)

# __str__による文字列化で表示可能
print(a) 

# 演算子のテスト
print(-a)
print(a + b)
print(a - b)
print(a * 0.5)

a += b
print(a)

# 正規化
print(a.normalized())

# 角度からベクトルを求める
print(Vector2.from_angle(45))