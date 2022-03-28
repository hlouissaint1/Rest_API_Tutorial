__author__ = "Himmler Louissaint"

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


#user = ('kara', 'nami')
#insert_user_query = "INSERT INTO users VALUES (NULL, ?, ?)"

#cursor.execute(insert_user_query, user)
#connection.commit()
#connection.close()
#
# users = [
#       ('Rolf', 'assf'),
#       ('Anne', 'beds'),
#       ('Rolf', 'assf'),
#       ('Jose', 'beds')
#  ]
# cursor.executemany(insert_user_query, users)
#connection.commit()
#connection.close()

insert_items_query = "INSERT INTO items VALUES (NULL, ?, ?)"
items = [
     ('piano', 1299),
     ('fridge', 499),
     ('laptop', 1499),
     ('mattress', 299),
     ('keyboard', 99),
     ('mouse', 9.99),
     ('monitor', 1299),
     ('television', 2499),
     ('table', 1499),
     ('handbag', 299),
     ('speaker', 99),
     ('wine', 9.99)]
cursor.executemany(insert_items_query, items)
connection.commit()
connection.close()