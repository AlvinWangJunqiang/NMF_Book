# -*- coding: utf-8 -*-
import c_nnmf
import a_sql_xls
import b_xls_mar
import numpy
import d_PQ_book_xls


def main():
   Pc=10
   book_number=10
   book_map,rating_map=a_sql_xls.mysql_xls("rating5.xls",book_number)
   mar=a_sql_xls.rating_matrix(book_map,rating_map)
   # print("mar=",mar)
   # mar=b_xls_mar.get_mar("rating4.xls")
   d_mar=numpy.matrix(mar)
   P,Q=c_nnmf.factorize(d_mar,Pc,iter=50)
   print ("user",len(mar))
   d_PQ_book_xls.PQ_xls(P,Q,"pq.xls",len(mar),Pc,len(book_map),book_map,Pc)


   print(P)
   print(Q)
