import csv
import sqlite3

con = sqlite3.connect('Notown-Records.db')
cur = con.cursor()

#table 1
create_table = '''CREATE TABLE albumInstrument(
                album_id INTEGER NOT NULL,
                instrument_id INTEGER NOT NULL,
                FOREIGN KEY (album_id) REFERENCES album (id) ON DELETE CASCADE,
                FOREIGN KEY (instrument_id) REFERENCES instrument (id)  ON DELETE CASCADE
                );
                '''

cur.execute(create_table)

file = open('album-instrument.csv')

contents = csv.reader(file)

insert_alb_inst = "INSERT INTO albumInstrument (album_id, instrument_id) VALUES(?,?)"

cur.executemany(insert_alb_inst, contents)

select_all = "SELECT * FROM albumInstrument"
rows = cur.execute(select_all).fetchall()

for r in rows:
    print(r)

file.close()

con.commit()

#table 2
create_table = '''CREATE TABLE album(
                title TEXT,
                id INTEGER,
                date INTEGER,
                type TEXT
                )
                '''

cur.execute(create_table)

file = open('album.csv')

contents = csv.reader(file)

insert_album = "INSERT INTO album (title, id, date, type) VALUES(?,?,?,?)"

cur.executemany(insert_album, contents)

select_all = "SELECT * FROM album"
rows = cur.execute(select_all).fetchall()

for r in rows:
    print(r)

con.commit()

file.close

#table3

create_table = '''CREATE TABLE instrument(
                id INTEGER,
                type TEXT,
                key TEXT
                
                )
                '''

cur.execute(create_table)

file = open('instrument.csv')

contents = csv.reader(file)

insert_instrument = "INSERT INTO instrument (id, type, key) VALUES(?,?,?)"

cur.executemany(insert_instrument, contents)

select_all = "SELECT * FROM instrument"
rows = cur.execute(select_all).fetchall()

for r in rows:
    print(r)

con.commit()

#table4

create_table = '''CREATE TABLE musicianAlbum(
                ssn INTEGER,
                album_id INTEGER,
                FOREIGN KEY (album_id) REFERENCES album (id)  ON DELETE CASCADE,
                FOREIGN KEY (ssn) REFERENCES musician (ssn)  ON DELETE CASCADE
                )
                '''

cur.execute(create_table)

file = open('musician-album.csv')

contents = csv.reader(file)

insert_musicianAlbum = "INSERT INTO musicianAlbum (ssn, album_id) VALUES(?,?)"

cur.executemany(insert_musicianAlbum, contents)

select_all = "SELECT * FROM musicianAlbum"
rows = cur.execute(select_all).fetchall()

for r in rows:
    print(r)

con.commit()

file.close

#table5

create_table = '''CREATE TABLE musician(
                name TEXT,
                ssn INTEGER
                )
                '''

cur.execute(create_table)

file = open('musician.csv')

contents = csv.reader(file)

insert_musician = "INSERT INTO musician (name, ssn) VALUES(?,?)"

cur.executemany(insert_musician, contents)

select_all = "SELECT * FROM musician"
rows = cur.execute(select_all).fetchall()

for r in rows:
    print(r)

con.commit()

file.close

#very end
con.close()