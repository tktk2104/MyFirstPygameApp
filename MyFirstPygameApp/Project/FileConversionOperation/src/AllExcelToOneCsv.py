import openpyxl
import csv
import glob

# 複数のExcelファイルの全データを格納するリスト
cell_data = []
# フォルダ内のエクセルファイルを変換
for excel_file_name in glob.glob("Project/FileConversionOperation/res/*.xlsx"):
    # デバッグ表示
    print(excel_file_name)
    # Excelのファイルを開く
    workbook = openpyxl.load_workbook(excel_file_name)
    # 先頭のシートを取得
    sheet = workbook.active
    # シート全体のデータをリストのリストに格納
    excel_data = [[cell.value for cell in row] for row in sheet]
    # 全データを格納するリストに結合
    cell_data.extend(excel_data);

# ファイルを書き込みモードでオープン(Windowsではnewline="\n")を指定
with open('Project/FileConversionOperation/res/output.csv', 'w', encoding='shift_jis', newline='\n') as file:
    # CSV書き込みオブジェクトを作成
    writer = csv.writer(file)
    # CSVに書き込み
    writer.writerows(cell_data)
