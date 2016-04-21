# -*- coding: UTF-8 -*-
import MySQLdb
import sys
import xlwt

def mysql_xls(xls_name):
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # 打开数据库连接
    db = MySQLdb.connect(user='root',db='user_map',passwd='122198',host='localhost',charset='utf8' )

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()

    #xls operation
    file = xlwt.Workbook() #注意这里的Workbook首字母是大写

    rating_sheet = file.add_sheet('rating',cell_overwrite_ok=True)
    user_sheet = file.add_sheet('user',cell_overwrite_ok=True)
    product_sheet = file.add_sheet('product',cell_overwrite_ok=True)
    user_map = dict()
    book_map = dict()
    rating_map=dict()
    i=0
    b=0
    # multilist = [[0 for col in range(5000)] for row in range(3000)]

    print "Database  : %s " % data

    #sql = "SELECT * FROM wait_map \
     #      WHERE tag > '%d'" % (0)
    sql = "SELECT * FROM STRUCT_MAP"


    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
       mysql_count=0
       for row in cursor:
          mysql_count+=1
          print ("mysql_count=",mysql_count)
          fname = row[0]
          book = row[1]
          rating=row[2]

          if fname not in user_map:
            user_map[fname]=i
            i=i+1
            user_sheet.write(user_map[fname],0,fname)
          # print fname
          # print user_map[fname]

          if book not in book_map:
             book_map[book]=b
             b=b+1
             product_sheet.write(book_map[book],0,book)
             print ("book unmber=",book_map[book])


          # try:
          #     index=rating.index('g')
          #     rating=rating[index+1:index+2]
          #     rating_sheet.write(user_map[fname],book_map[book],int(rating))
          # except:
          #     rating_sheet.write(user_map[fname],book_map[book],2)


          if rating=='date':
              print "rating is data make it one"
              addtwodimdict(rating_map, user_map[fname], book_map[book], 2)
          else:
            index=rating.find('rating')
            sStr1 = rating[index + 6:index+7]
            print sStr1
            addtwodimdict(rating_map, user_map[fname], book_map[book], int(sStr1))
    except:
       print "mysql_xls Finish !!"


    file.save(xls_name)
    # 关闭数据库连接
    db.close()
    return user_map,book_map,rating_map


def addtwodimdict(thedict, key_a, key_b, val):
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})


def rating_matrix(user_map,book_map,rating_map):
    multilist = [[0 for row in range(len(book_map))] for col in range(len(user_map))]
    print ("rating_map",len(user_map),len(book_map))
    for i in range(len(user_map)):
        for j in range(len(book_map)):
            print i,j
            if i in rating_map:
                if j in rating_map[i]:
                 print ("rat.....",rating_map[i][j])
                 multilist[i][j]=rating_map[i][j]
            else:
                 multilist[i][j]=0

    return  multilist




def main():

   a,b,c=mysql_xls("rating5.xls")
   mar=rating_matrix(a,b,c)
   print c
   print("mar=",mar)


if __name__=="__main__":
    main()

