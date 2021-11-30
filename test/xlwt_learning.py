import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("sheet_1")
cheng_fa_biao = workbook.add_sheet("cheng_fa_biao")
worksheet.write(0,0,"helloo")
for i in range(9):
    for j in range(i+1):
        cheng_fa_biao.write(i, j, (i+1)*(j+1))




workbook.save("test.xls")
