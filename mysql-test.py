import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', db='test',
        user='qinkun', passwd='qinkun')
cur = conn.cursor()

#r = cur.execute('insert into people values(6,\'Bill Gates\',58,\'M\')')
#cur.execute('delete from people where age=58')
#conn.commit()

r = cur.execute('select * from test')
r = cur.fetchall()
print r