#import openpyxl
import xlrd

book = xlrd.open_workbook("D:\\Projects\\pythonSeleniumFrameworkBatch_1\\ExcelData.xls")
#book1 = openpyxl.load_workbook("D:\\Projects\\pythonSeleniumFrameworkBatch_1\\ExcelData.xls")

#sheet1 = book1.active
sheet = book.sheet_by_index(0)

#cell1  = sheet1.cell(row=1,column=1)
cell = sheet.cell(rowx=0, colx=0).value
print(cell)

rows = sheet.get_rows()

print(rows)

columns = sheet.utter_max_cols

print(columns)

#sheet.cell(rowx=2, colx=0).value = "Mohan"  # write

