import sqlite3
import os.path

print('SQLite version:')
print(sqlite3.version)

print('Loading the Database')
con = sqlite3.connect('hw8.db')
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





print('Q1: For each sailor (sid) who previously reserved a boat, find the total number of boats reserved by he/she')

print('Your answer should have two attributes: sid and count')


'''
Please Write Down Your Query for Q1 Below:
'''

#answer = "SELECT R.sid , COUNT(1) FROM Reserve R WHERE (SELECT DISTINCT B.bid FROM Boat B WHERE B.bid = R.bid) GROUP BY R.sid "
answer = '''
SELECT R.sid , COUNT(DISTINCT B.bid)
FROM Boat B, Reserve R
WHERE B.bid = R.bid
GROUP BY R.sid
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')


print('Q2: For each sailor (sid), find the total number of reservation made by the sailor. We only return the sailor who have at least two reservations')

print('Your answer should have two attributes: sid and count')


'''
Please Write Down Your Query for Q2 Below:
'''

answer = '''
SELECT R.sid, COUNT(R.sid)
FROM Boat B, Reserve R
WHERE B.bid = R.bid
GROUP BY R.sid
HAVING COUNT(*)>=2
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')


print('Q3: For each name of the sailors (sname), find the total number of distinct red boats reserved by them. We only return the sailors who reserved at least two distinct boats')
print('Your answer should have two attributes: sname and count')


'''
Please Write Down Your Query for Q3 Below:
'''

answer = '''
SELECT S.sname, COUNT(B.color)
FROM Boat B, Reserve R, Sailor S
WHERE B.bid = R.bid AND S.sid = R.sid AND B.color = 'red'
GROUP BY R.sid
HAVING COUNT(*)>=2
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')