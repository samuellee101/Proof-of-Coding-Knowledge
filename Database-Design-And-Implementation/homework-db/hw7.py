import sqlite3
import os.path

print('SQLite version:')
print(sqlite3.version)

print('Loading the Database')
con = sqlite3.connect('hw7.db')
cur = con.cursor()
print('Success!')
print('Print the Whole Dataset:')

t = cur.execute('SELECT * FROM Sailor')
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')

t = cur.execute('SELECT * FROM Boat')
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t: print(row)
print('--------------------')

t = cur.execute('SELECT * FROM Reserve')
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t: print(row)
print('--------------------')



print('Q0: This is an example question. Find the Name of the all Sailors')

'''
Please Write Down Your Query for Q0 Below:
'''

answer = "SELECT sname FROM Sailor"


t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')



print('Q1: Find the name of the sailors who is a female')

'''
Please Write Down Your Query for Q1 Below
'''

answer = "SELECT sname FROM Sailor WHERE gender = 'F'"


t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')


import sqlite3
import os.path

print('Q2: Find the name of the boat which is reserved by at least one female sailor')

'''
Please Write Down Your Query for Q2 Below:
'''

#answer = "SELECT bname FROM Boat WHERE Boat INTERSECT (SELECT sid FROM Sailor WHERE gender = 'F' INTERSECT SELECT sid FROM RESERVE)"
#answer = "SELECT bname FROM (Boat UNION (Sailor UNION Reserve)) WHERE gender = 'F'"
answer = "SELECT DISTINCT bname FROM Boat B, Sailor S, Reserve R WHERE S.gender = 'F' AND S.sid = R.sid AND R.bid = B.bid"

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')


print('Q3: Find the boat (bid) which is only reserved by male sailors')


'''
Please Write Down Your Query for Q3 Below
'''

answer = "SELECT bid FROM Sailor, Reserve ON Reserve.sid = Sailor.sid WHERE Sailor.gender = 'M' AND bid NOT IN (SELECT bid FROM Sailor, Reserve ON Reserve.sid = Sailor.sid WHERE Sailor.gender='F')"


t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')
