# -*- coding: utf-8 -*-
import xlrd

def get_mar(fname):

    bk = xlrd.open_workbook(fname)

    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("rating")
    except:
        print "no sheet in %s named Sheet1" % fname

    nrows = sh.nrows
    ncols = sh.ncols
    # print "nrows %d, ncols %d" % (nrows,ncols)

    cell_value = sh.cell_value(0,0)
    print cell_value

    row_list = []
    for i in range(1,nrows):
        row_data = sh.row_values(i)
        # print "new line"
        # print row_data
        for index, item in enumerate(row_data):
            if not item:
             # print item
             row_data[index]=1
        row_list.append(row_data)

    print "matrix:"
    print row_list
    return row_list
