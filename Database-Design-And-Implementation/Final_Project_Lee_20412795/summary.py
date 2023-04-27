import sqlite3

con = sqlite3.connect('Notown-Records.db')
cur = con.cursor()

print("Number of musicians: \n")

answer = '''
SELECT COUNT(musician.name) AS number
FROM musician
WHERE musician.name != 'name'
'''
#offset because it counts the first row

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')


print("\n\nList of musicians: \n")

answer = '''
SELECT musician.name, musician.ssn
FROM musician
WHERE musician.name != 'name'
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')

print("\n\nTotal number of albums: \n")

answer = '''
SELECT COUNT(album.title) AS number
FROM album
WHERE album.title != 'title'
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')

print("\n\nAlbum list: \n")

answer = '''
SELECT album.title, album.id, date, type
FROM album
WHERE album.title != 'title'
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')

print("\n\nTotal number of instruments: \n")

answer = '''
SELECT COUNT(instrument.id) AS number
FROM instrument
WHERE instrument.id != 'id'
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')

print("\n\nList of instruments \n")

answer = '''
SELECT id, type, key
FROM instrument
WHERE instrument.id != 'id'
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')

print("\n\nA table consists of the name of musicians and the total number of albums written by them. \n")

answer = '''
SELECT musician.name, COUNT(album_id) AS 'number of albums'
FROM musicianAlbum, musician
WHERE musician.ssn = musicianAlbum.ssn
GROUP BY musician.ssn
'''

t = cur.execute(answer)
names = list(map(lambda x: x[0], t.description))
print(names)
print('--------------------')
for row in t : print(row)
print('--------------------')



#very end
con.close()