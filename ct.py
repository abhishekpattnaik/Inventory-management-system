import sqlite3

conn= sqlite3.connect("NaaSClue_DATABASE.db")
conn.execute("CREATE TABLE ITEMS(I_ID INT PRIMARY KEY NOT NULL,I_NAME TEXT NOT NULL,QUANTITY INT NOT NULL,PRICE INT NOT NULL);")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (101,'dal',0,68)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (102,'wheat',300,45)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (103,'barley',500,54)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (104,'oats',40,54)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (105,'peanuts',450,45)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (106,'onion',3,54)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (107,'garlic',44,56)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (108,'ginger',440,54)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (109,'mustard',430,34)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (110,'jeera',443,43)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (111,'salt',434,54)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (112,'pepper',443,34)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (113,'black salt',434,34)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (114,'black pepper',345,43)")
conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (115,'potato',345,34)")
print("thank you \n database created")
conn.commit()