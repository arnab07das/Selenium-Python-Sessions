import xlrd

workbook = xlrd.open_workbook("E:\Python\Python Data\DataFile.xls")
sheet = workbook.sheet_by_name("Login")

#Get the Row and Column Count
rows = sheet.nrows
columns = sheet.ncols

print(rows,columns)

for i in range (1,rows):
    username = sheet.cell_value()