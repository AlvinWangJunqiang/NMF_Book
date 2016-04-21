# -*- coding: UTF-8 -*-
import xlwt
import numpy

def PQ_xls(a,b,xls_name,prow,pcol,qcol,book_map,Pc):

    a=a.tolist()
    b=b.tolist()
    #xls operation
    array_cat_map=dict()

    file = xlwt.Workbook() #注意这里的Workbook首字母是大写

    P_sheet = file.add_sheet('P',cell_overwrite_ok=True)
    Q_sheet = file.add_sheet('Q',cell_overwrite_ok=True)


    class_gold=[[0 for row in range(10)] for col in range(pcol)]

    for p_row in range(prow):
     for p_col in range(pcol):
        # print a[p_row][p_col]
        P_sheet.write(p_row,p_col,a[p_row][p_col])
    for q_row in range(pcol):
     for q_col in range(qcol):
        # print (b[q_row][q_col])
        Q_sheet.write(q_col,q_row,b[q_row][q_col])
         # for i in range(10):
         #     if class_gold[q_row][i]

    for Pc_i in range(Pc):
     for key in book_map:
         Q_sheet.write(int(book_map[key]),q_row+1,key)
         cat_array =list

         array_cat_map[key]=b[Pc_i][int(book_map[key])]
         # array_cat_map[key]=cat_array
     sorted2=sorted(array_cat_map.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
     cat_array_number=0
     for sorted_i in sorted2 :
       cat_array_number+=1
       Q_sheet.write(cat_array_number,q_row+3+Pc_i*2,sorted_i[0])
       Q_sheet.write(cat_array_number,q_row+4+Pc_i*2,sorted_i[1])

    file.save(xls_name)
    # 关闭数据库连接


