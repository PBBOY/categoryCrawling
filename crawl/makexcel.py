import openpyxl
import math

arr = [1,2, 3, 4, 5, 6]

wb = openpyxl.load_workbook('test.xlsx')

for i in arr:
    wb.create_sheet(index=0, title='Sheet No. '+str(i))
    sheet = wb.active
    index = i
    if 0 > 3:
        index = i/2

    sheet['A'+str(index)] = 'SFU'+str(i)

wb.save('test.xlsx')
