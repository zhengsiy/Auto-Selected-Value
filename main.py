import openpyxl

#在这个路径下打开英雄表格
wb = openpyxl.load_workbook("files/ACG_Hero.xlsm")

#获取所有表的表名
sheet_names = wb.sheetnames
print(f"表格中有这些sheet：{sheet_names}")

#获取活动表对应的表对象，即需要处理数据的那个表
active_sheet = wb["ACG_Hero"]
print((active_sheet))

