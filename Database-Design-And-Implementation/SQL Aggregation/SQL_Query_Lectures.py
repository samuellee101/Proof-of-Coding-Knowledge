#!/usr/bin/env python
# coding: utf-8

# # SQLite3 Connection

# In[1]:


import sqlite3
con = sqlite3.connect('CSCI4333_Sailor.db')
cursor = con.cursor()


# # Functions to print table info

# In[7]:


def print_table(table_name="Sailors"):
    res_table = cursor.execute("SELECT * FROM "+table_name)
    attribute = [x[0] for x in res_table.description]
    print(attribute)
    print('--------------')
    for row in res_table: print(row)

def print_query_res(res_table):
    #res_table = cursor.execute("SELECT * FROM "+table_name)
    attribute = [x[0] for x in res_table.description]
    print(attribute)
    print('--------------')
    for row in res_table: print(row)


# In[3]:


print_table("Reserves")


# In[4]:


print_table("Boats")


# In[5]:


print_table("Sailors")


# # Simple Queries

# Q1: Find the name of the Sailor who reserved boat 103?

# In[10]:


#Solution 1: Basic Query
statement = "SELECT sname FROM Sailors S,Reserves R WHERE S.sid=R.sid AND R.bid='103'"
res_table = cursor.execute(statement)
print_query_res(res_table)


# In[12]:


#Solution 2: Nested Query
statement = '''
SELECT sname FROM Sailors S 
WHERE S.sid IN (SELECT R.sid FROM Reserves R WHERE R.bid='103')
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# In[14]:


#Solution 3: Natural Join Solution
statement = "SELECT sname FROM Sailors S NATURAL JOIN Reserves R WHERE R.bid='103'"

res_table = cursor.execute(statement)
print_query_res(res_table)


# In[15]:


#Solution 4: Inner Join Solution
statement = "SELECT sname FROM Sailors S INNER JOIN Reserves R ON S.sid=R.sid WHERE R.bid='103'"

res_table = cursor.execute(statement)
print_query_res(res_table)


# In[18]:


#Solution 5: Correlated Nested Query
statement = '''
SELECT sname FROM Sailors S 
WHERE EXISTS (SELECT * FROM Reserves R WHERE R.bid='103' AND R.sid=S.sid)
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# # Aggregation Query

# Q2: Find the maximal rating of the sailors whose age is greater than 18

# In[19]:


statement = '''
SELECT MAX(S.rating) FROM Sailors S 
WHERE S.age>18
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q3: Find the mimimal age for each rating stored in the database. You answer should contains (rating, age)

# In[23]:


statement = '''
SELECT S.rating, MIN(S.age) 
FROM Sailors S
GROUP BY S.rating
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q4: Find the mimimal age for each rating stored in the database. We only consider the sailor whose age is greater or equal to 18. You answer should contains (rating, age)

# In[22]:


statement = '''
SELECT S.rating, MIN(S.age) 
FROM Sailors S
WHERE S.age>=18 
GROUP BY S.rating
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q5: for each rating that has at least two sailors, find the mimimal age for each rating. We only consider the sailor whose age is greater or equal to 18. You answer should contains (rating, age)

# In[25]:


statement = '''
SELECT S.rating, MIN(S.age) 
FROM Sailors S
WHERE S.age>=18 
GROUP BY S.rating
HAVING COUNT(*)>1
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q6: Find the average rating for each age stored in the database. You answer should contains (age, rating)

# In[27]:


#For every age of sailors, find the average rating
statement = '''
SELECT S.age, AVG(S.rating) 
FROM Sailors S
GROUP BY S.age
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q7: Find the count of boats for each boat color stored in the database. You answer should contains (color, count)

# In[31]:




statement = '''
SELECT B.color, COUNT(*) 
FROM Boats B
GROUP BY B.color
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q8: Find the count of reservations for each boat color stored in the database. You answer should contains (color, count)

# In[34]:


#For every color of the boat, count how many times the sailors reserved the boats

statement = '''
SELECT B.color,COUNT(sid)
FROM Boats B, Reserves R
WHERE B.bid = R.bid
GROUP BY B.color
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q9: Find the count of unique sailors for each boat color stored in the database. You answer should contains (color, count)

# In[36]:


#For every color of the boat, count how many unique sailors who reserved the boats

statement = '''
SELECT B.color,COUNT(DISTINCT sid)
FROM Boats B, Reserves R
WHERE B.bid = R.bid
GROUP BY B.color
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q10: Find the count of unique sailors for each boat color stored in the database. You answer should contains (color, count)

# In[ ]:


#For every color of the boat, count how many unique sailors who reserved the boats

statement = '''
SELECT B.color,COUNT(DISTINCT sid)
FROM Boats B, Reserves R
WHERE B.bid = R.bid
GROUP BY B.color
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q11: Find the average age of the reservations for each boat stored in the database. You answer should contains (bid, age)

# In[38]:


statement = '''
SELECT R.bid, AVG(S.age)
FROM Reserves R, Sailors S
WHERE S.sid=R.sid
GROUP BY R.bid
'''
res_table = cursor.execute(statement)
print_query_res(res_table)


# Q12: For each boat which reserved by at least three unique sailors, find the average age of the reservations for each boat stored in the database. You answer should contains (bid, age)

# In[40]:


statement = '''
SELECT R.bid, AVG(S.age)
FROM Reserves R, Sailors S
WHERE S.sid=R.sid
GROUP BY R.bid
HAVING COUNT(DISTINCT S.sid)>=3
'''
res_table = cursor.execute(statement)
print_query_res(res_table)


# Q13: For each boat which reserved by at least two unique sailors that rating are greater than 5, find the average age of the reservations for each boat stored in the database. You answer should contains (bid, age)

# In[46]:


statement = '''
SELECT R.bid, AVG(S.age)
FROM Reserves R, Sailors S
WHERE S.sid=R.sid AND S.rating>5
GROUP BY R.bid
HAVING COUNT(DISTINCT S.sid)>=2
'''
res_table = cursor.execute(statement)
print_query_res(res_table)


# Q13: For each boat which reserved by at least one sailor whose age is less than 35, find the average age of the reservations for each boat stored in the database. You answer should contains (bid, age)

# In[48]:


#For each boat (bid) which reserved by at least one sailor 
#whose age is less than 20,find the average rating of the 
#sailors who reserved it

statement = '''
SELECT R.bid, AVG(S.age)
FROM Reserves R, Sailors S
WHERE S.sid=R.sid
GROUP BY R.bid
HAVING MIN(S.age)<=35
'''
res_table = cursor.execute(statement)
print_query_res(res_table)


# Q14: Find the name for the sailors who reserved at least two boats.

# In[53]:


statement = '''
SELECT S.sname
FROM Sailors S, Reserves R
WHERE S.sid=R.sid
GROUP BY S.sid, S.sname
HAVING COUNT(bid)>=2
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# # Aggregation + Nested Query 

# Q15: Find the name for the sailors who reserved at least two boats. (Using nested query)

# In[55]:


statement = '''
SELECT S.sname
FROM Sailors S
GROUP BY S.sid, S.sname
HAVING (SELECT COUNT(bid) FROM Reserves R WHERE S.sid=R.sid)>=2
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q16: Find the name of sailors who reserved at least two times red boats (Using nested query)

# In[57]:


statement = '''
SELECT S.sname
FROM Sailors S
GROUP BY S.sid, S.sname
HAVING (SELECT COUNT(bid) 
        FROM Reserves R 
        WHERE S.sid=R.sid AND
        R.bid IN (
                   SELECT B.bid FROM Boats B WHERE B.color='red'
                 )
       )>=2
'''

res_table = cursor.execute(statement)
print_query_res(res_table)


# Q17: For each boat (bid) which reserved by at least two unique sailors, find the average rating of the sailors who reserved it. Note: We count each sailor only once

# In[66]:


#For each boat (bid) which reserved by at least two sailor 
#find the average rating of the sailors who reserved it. 
#Note: We count each sailor only once!

statement = '''
SELECT T.sid, AVG(T.rating) 
FROM  (SELECT DISTINCT S.sid,R.bid,S.rating
       FROM Reserves R, Sailors S
       WHERE R.sid=S.sid) AS T
GROUP BY T.sid
HAVING COUNT(sid)>=2
'''

res_table = cursor.execute(statement)
print_query_res(res_table)



# Q18: Return the name of sailor(s) who reserved the highest number of boats

# In[68]:


statement = '''
SELECT sname 
FROM Sailors S, Reserves R
WHERE S.sid = R.sid 
GROUP BY S.sid, S.sname
HAVING COUNT(*)=(SELECT MAX(T.c) 
                 FROM (SELECT R2.sid, COUNT(*) AS c 
                       FROM Reserves R2 
                       GROUP BY R2.sid) AS T
                 )
'''


res_table = cursor.execute(statement)
print_query_res(res_table)

