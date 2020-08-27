import csv # CSVファイル用のモジュール
 
# ヘッダー
header = ['ID', 'name']
# 内容
body = [
  [0, '鈴木'],
  [1, '田中'],
  [2, '山田']
]
 
# ファイルを書き込みモードでオープン
# Windowsでは改行コードを’\n’に指定
# Excelで開く場合は、文字コードをSJISに指定）
file = open('Project/CsvFileOperation/res/test.csv', 'w', encoding='shift_jis', newline='\n')
# csv書き込みオブジェクトを作成
writer = csv.writer(file)
# 1次元配列(リスト）で１行書き込み
writer.writerow(header)
# ２次元配列(リストのリスト）でまとめて書き込み
writer.writerows(body)
# ファイルを閉じる
file.close()