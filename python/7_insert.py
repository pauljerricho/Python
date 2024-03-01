from openpyxl import load_workbook
wb = load_workbook("sample3.xlsx")
ws = wb.active

ws.insert_rows(8) # 8번째 줄이 비워짐
ws.insert_rows(8, 5) # 8번째 줄로부터 5줄을 추가

ws.insert_cols(2) # 4번째 열이 비워짐
ws.insert_cols(2, 3) # 4번째 열로부터 3열이 추가됨

wb.save("sample_insert.xlsx")