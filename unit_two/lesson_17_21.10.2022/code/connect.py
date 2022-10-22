import sys
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=auth user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

name  = str(input("Введите логин:"))
paswd = str(input("Введите пароль:"))
SQL = f"""select a.login, a."password", p.surname
            from account a, profile p
           where a.id_profile = p.id
             and a.login like '{name}'"""
# Execute a query
cur.execute(SQL)

# Retrieve query results
records = cur.fetchone()
login, passwd_, surname = records
if paswd != passwd_:
    sys.exit("Access denied")


print(records)

