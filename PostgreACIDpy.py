# Python / PostgreSQL 
# ACID is implemented

# pip install psycopg2
# pip install tabulate

import psycopg2
from tabulate import tabulate


print('Beginning')

con = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='CognerObas1976.')

print(con)

#For isolation: SERIALIZABLE It makes sure changes happen one after the other in the event mulitple users
#Are connecting and updating the system at the same time 
con.set_isolation_level(3)

#For atomicity. Specifics whether changes made to the database is committed or not 
con.autocommit = False

try:
    cur = con.cursor()
    # QUERY Constraint is dropped
    # The depot d1 changes its name to dd1 in Depot and Stock
    cur.execute("ALTER table stock DROP CONSTRAINT stock_depid_fkey")
    cur.execute("UPDATE depot SET addr='dd1' WHERE depid='d1'")
    cur.execute("UPDATE Stock SET depid = 'dd1' WHERE depid ='d1'")

except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transaction could not be completed so database will be rolled back")
    con.rollback()

finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection: closed")
