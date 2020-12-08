import xlrd
import os
def get_data(filename,sheetnum):
    path1=os.path.realpath(__file__).split('C')[0]
    # print(path1)
    file = 'data\logon1.xlsx'
    path=os.path.join(path1,file)
    # print(path)

    book_data=xlrd.open_workbook(path)
    book_sheet=book_data.sheet_by_index(0)
    row0=book_sheet.row_values(0)
    nrows=book_sheet.nrows
    ncols=book_sheet.ncols
    list=[]
    for i in range(1,nrows):
        row_data=book_sheet.row_values(i)
        row_dir={}
        for j in range(0,ncols):
            row_dir[row0[j]]=row_data[j]
        list.append(row_dir)
    # print(list)
    return list


get_data('',1)