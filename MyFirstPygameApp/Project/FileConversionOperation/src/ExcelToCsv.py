import openpyxl # Excelファイル操作
import csv      # CSVファイル操作
import glob     # フォルダ操作
import os       # ファイル名の操作
 
# フォルダ内のエクセルファイルを変換
for excel_file_name in glob.glob("Project/FileConversionOperation/res/*.xlsx"):
    # Excelファイル名をデバッグ表示
    print(excel_file_name)
    # Excelのファイルを開く
    workbook = openpyxl.load_workbook(excel_file_name)
    # 先頭のシートを取得
    sheet = workbook.active
    # シート全体のデータをリストのリストに格納
    cell_data =[[cell.value for cell in row] for row in sheet]

    # Excelファイル名と拡張子を分離する
    file_name, file_ext = os.path.splitext(excel_file_name)
    # 拡張子をcsvファイルに変更
    csv_file_name = file_name + ".csv"
    # ファイルを書き込みモードでオープン(Windowsではnewline='\n')を指定
    with open(csv_file_name, 'w', encoding="shift_jis", newline='\n') as file:
        # csv書き込みオブジェクトを作成
        writer = csv.writer(file)
        # csvに書き込み
        writer.writerows(cell_data)