import os
import os.path
from xlutils.copy import  copy
from xlrd import  open_workbook
import os
from xlwt import *

def writesize(y,filenameitem,size_number):

    rb = open_workbook('result.xls', formatting_info=True)
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(y, 0, filenameitem)
    sheet.write(y, 1,size_number/1024)
    wb.save('result.xls')


def writeheap():
    file = Workbook(encoding='utf-8')
    table = file.add_sheet('Sheet')
    table.write(0, 0, u'version')
    table.write(0, 1, u'size')
    file.save('result.xls')



def main():
    y =1
    writeheap()
    rootdir = os.getcwd() + '/apk/'
    for parent,dirnames,filenames in os.walk(rootdir):
        for fileitem in filenames:
            if fileitem.endswith('.apk'):
                filenameitem=fileitem.split('.apk')
                print os.path.join(parent,fileitem)
                size_number = os.path.getsize(os.path.join(parent,fileitem))
                writesize(y,filenameitem,size_number)
                y+=1



if __name__ == '__main__':

    main()
