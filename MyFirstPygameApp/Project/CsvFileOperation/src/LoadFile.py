import csv # CSVファイル用のモジュール
 
try:
    # ファイルを読み込みモードでオープン
    with open('Project/CsvFileOperation/res/test.csv', 'r', encoding='shift_jis') as file:
        # csv読み込みクラスを作成
        reader = csv.reader(file)
        # 行単位で読み込み
        for row in reader:
            # 行からセルを1個ずつ取得
            for cell in row:
                print(cell, end=' ')
            print()
except:
    print('読み込みエラーが発生!')


## ファイルを読み込みモードでオープン
#file = open('Project/CsvFileOperation/res/test.csv', 'r', encoding='shift_jis')
## csv読み込みクラスを作成
#reader = csv.reader(file)
#
### 最初の１行目（ヘッダ部分）をスキップ
##next(reader)
#
## 行単位で読み込み
#for row in reader:
#    # 行からセルを1個ずつ取得
#    for cell in row:
#        print(cell, end=' ')
#    print()
## ファイルを閉じる
#file.close()

## ファイルを読み込みモードでオープン
#file = open('Project/CsvFileOperation/res/test.csv', 'r', encoding='shift_jis')
## csv読み込みクラスを作成
#reader = csv.reader(file)
## データを２次元配列（リストのリストに格納）
#data = [ [cell for cell in row] for row in reader]
## ファイルを閉じる
#file.close()