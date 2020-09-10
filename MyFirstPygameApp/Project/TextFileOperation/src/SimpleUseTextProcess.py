
## まずは読み込み処理

## とりあえず開いてみた
with open('Project/TextFileOperation/res/input.csv', 'r', encoding='shift_jis') as file:
    for line in file:
        print(line, end='')

## リストに格納してみた
with open('Project/TextFileOperation/res/input.csv', 'r', encoding='shift_jis') as file:
    lines = file.readlines();
    for line in lines:
        print(line, end='') 

## 改行文字を消してみた
with open('Project/TextFileOperation/res/input.csv', 'r', encoding='shift_jis') as file:
    lines = [line.rstrip() for line in file.readlines()]
    for line in lines:
        print(line, end='')

## そもそも改行文字が付かない方法で読み込んでみた
with open('Project/TextFileOperation/res/input.csv', 'r', encoding='shift_jis') as file:
    lines = file.read().splitlines()
    for line in lines:
        print(line, end='')

## 自力でcsvファイルの情報を読み込んでみた
with open('Project/TextFileOperation/res/input.csv', 'r', encoding='shift_jis') as file:
    for line in file.read().splitlines(): # 行単位で読み込む
        for cell in line.split(','): # カンマ区切りに分割
            print(cell + ' ', end='')
        print()

## 合計値を出してみた
sum = 0
with open('Project/TextFileOperation/res/input.csv') as file:
    for line in file.read().splitlines():
        for num in line.split(','):
            sum += int(num)
print(sum)

##------------------------------------------------------------------------------------------------------------------------------------------------------
## ここから書き込み処理

## とりあえず書き込んでみた
with open('Project/TextFileOperation/res/outputA.csv', 'w', encoding='shift_jis', newline='\n') as file:
    file.write('1,2,3\n')
    file.write('4,5,6\n')


## リストの文字列をそのまま書き込んでみた
lines = ['1,2,3\n', '4,5,6\n']
with open('Project/TextFileOperation/res/outputB.csv', 'w', encoding='shift_jis') as file:
    file.writelines(lines)

## 改行文字の無いリストの文字列を書き込んでみた
lines = ['1,2,3', '4,5,6']
with open('Project/TextFileOperation/res/outputC.csv', 'w', encoding='shift_jis') as file:
    file.write('\n'.join(lines))

## 2次元配列はcsv形式で書き込んでみた
lines = [[1, 2, 3], [4, 5, 6]]
with open('Project/TextFileOperation/res/outputD.csv', 'w', encoding='shift_jis') as file:
    for line in lines:
        file.write(','.join(map(str, line)) + '\n')