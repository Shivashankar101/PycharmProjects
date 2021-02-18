import csv


file = '/Users/shiv/Desktop/logindata.csv'
data = open(file, encoding="utf-8")
csv_reader = csv.reader(data)
data_lines = list(csv_reader)
for line in data_lines:
    print(line[4])
#
#
# def count_rows(file_path, sheetname):
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook.get_sheet_by_name(sheetname)
#     return sheet.max_row
#
# def count_clos(file_path, sheetname):
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook.get_sheet_by_name(sheetname)
#     return sheet.max_column
#
# def read_data(file_path, sheetname, row, col):
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook.get_sheet_by_name(sheetname)
#     return sheet.cell(row=row, column=col).value
#
# def write_data(file_path, sheetname, row, col, data):
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook.get_sheet_by_name(sheetname)
#     return (sheet.cell(row=row, column=col).value == data)
#     workbook.save(file_path + '.xlsx')






