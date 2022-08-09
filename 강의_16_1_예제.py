from sqlite3 import *

con = connect("phone_list.db")
cur = con.cursor()

#생성
#cur.execute('create table Booklist1(Name text,Page text);')

#데이터삽입
#cur.execute('insert into Booklist1 values("한국사","300")')
#cur.execute('insert into Booklist1 values("중국사","200")')

#값 수정
#cur.execute('update Booklist1 Set Name=? where Name=?'
#            ,('한국사','중국사'))

#값 삭제
cur.execute('delete from Booklist1 where Name=?',('한국사',))


con.commit()
con.close()
