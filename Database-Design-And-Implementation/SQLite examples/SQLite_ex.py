#!/usr/bin/env python
# coding: utf-8

# # SQLite3 Connection

# In[25]:


import sqlite3
con = sqlite3.connect('CSCI4333_Sailor.db')
cursor = con.cursor()


# # Create Table

# In[5]:


#cursor.execute("DROP TABLE Sailors")
text= '''
CREATE TABLE Sailors (
sid text,
sname text,
rating int,
age int,
PRIMARY KEY (sid)
);
'''

cursor.execute(text)

#cursor.execute("DROP TABLE Boats")

text= '''
CREATE TABLE Boats (
bid text,
bname text,
color text,
PRIMARY KEY (bid)
);
'''
cursor.execute(text)

#cursor.execute("DROP TABLE Reserves")

text= '''
CREATE TABLE Reserves (
sid text,
bid text,
day date,
PRIMARY KEY (sid,bid),
FOREIGN KEY(sid) REFERENCES Sailors(sid),
FOREIGN KEY (bid) REFERENCES Boats(bid)
);
'''
cursor.execute(text)


# # INSERT Data Sailor Example

# In[8]:


cursor.execute("INSERT INTO Sailors VALUES ('22','Dustin',7,45)")
cursor.execute("INSERT INTO Sailors VALUES ('29','Brutus',1,35)")
cursor.execute("INSERT INTO Sailors VALUES ('31','Lubber',8,55)")
cursor.execute("INSERT INTO Sailors VALUES ('32','Andy',8,25)")
cursor.execute("INSERT INTO Sailors VALUES ('58','Rusty',10,35)")
cursor.execute("INSERT INTO Sailors VALUES ('64','Horatio',7,35)")
cursor.execute("INSERT INTO Sailors VALUES ('71','Zorda',10,16)")
cursor.execute("INSERT INTO Sailors VALUES ('74','Horatio',9,35)")
cursor.execute("INSERT INTO Sailors VALUES ('85','Art',3,25)")
cursor.execute("INSERT INTO Sailors VALUES ('95','Bob',3,63)")


# # INSERT Data Boats Example

# In[ ]:


def insert_boats(cursor, param):
    command = "INSERT INTO Boats VALUES (?,?,?)"
    cursor.execute(command, param)

insert_boats(cursor, ('103','Clipper','green'))
insert_boats(cursor, ('104','Marine','red'))


# # Import Data From CSV File Example

# In[ ]:


records = open('reserve.csv','r').readlines()

data = tuple(records[1].replace('\n','').split(','))

def insert_reserves(cursor, param):
    command = "INSERT INTO Reserves VALUES (?,?,?)"
    cursor.execute(command, param)


for i in range(1,len(records)):
    data = tuple(records[i].replace('\n','').split(','))
    insert_reserves(cursor, data)


# # Functions to print table info

# In[26]:


def print_table(table_name="Sailors"):
    res_table = cursor.execute("SELECT * FROM "+table_name)
    attribute = [x[0] for x in res_table.description]
    print(attribute)
    print('--------------')
    for row in res_table: print(row)


# In[27]:


print_table("Reserves")


# In[ ]:


print_table("Boats")


# In[ ]:


print_table("Sailors")


# In[73]:


con.commit()


# # Example Queries

# In[28]:


#Find the name of the Sailor who reserved boat 103?

def print_query_res(res_table):
    #res_table = cursor.execute("SELECT * FROM "+table_name)
    attribute = [x[0] for x in res_table.description]
    print(attribute)
    print('--------------')
    for row in res_table: print(row)
        


# In[31]:


statement = "SELECT sname FROM Sailors S,Reserves R WHERE S.sid=R.sid AND R.bid='103'"
res_table = cursor.execute(statement)

print_query_res(res_table)


# In[32]:


statement = '''
SELECT sname FROM Sailors S 
WHERE S.sid IN (SELECT R.sid FROM Reserves R WHERE R.bid='103')
'''

res_table = cursor.execute(statement)
print_table2(res_table)


# In[33]:


statement = '''
SELECT MAX(S.rating) FROM Sailors S
'''

res_table = cursor.execute(statement)
print_table2(res_table)


# In[34]:


statement = '''
SELECT * FROM Sailors S
'''

res_table = cursor.execute(statement)
print_table2(res_table)


# In[ ]:




