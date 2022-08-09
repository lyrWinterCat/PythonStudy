

from sqlite3 import *


con = connect("C:\\DBMS\\Person_list.db")
cur = con.cursor()


cur.execute("SELECT * FROM list")

# fetchone(): 행 단위로 데이터를 읽는 메서드
#            반환값 = 튜플값 
'''
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())  >>>None 반환
'''
# 몇개인지 모르면?
#for row in cur:
#    print(row)

# 전체 내용을 한번에 읽어오는 메서드
# fetchall()

f = cur.fetchall()
print(f)
print("타입>",type(f))
#>>>list 타입!


con.commit() 
con.close()
