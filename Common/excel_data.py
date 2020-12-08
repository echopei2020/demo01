import xlrd,os
def read_excel(filename,index):
    xls=xlrd.open_workbook(filename)
    sheet=xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)
    dic={}

    for i in range(1,sheet.nrows):
        data=[]
        for j in range(sheet.ncols):
            data.append((sheet.row_values(i)[j]))
        dic[i]=data
    return dic

if __name__=='__main__':
    #filename=r'F:\auto test data\logon.xlsx'
    data=read_excel(os.path.split(os.path.realpath(__file__))[0].split('C')[0]+"Data\\logon1.xlsx",0)
    # data=read_excel(filename,0)
    print(data)
