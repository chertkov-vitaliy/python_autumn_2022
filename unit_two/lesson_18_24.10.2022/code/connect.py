import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


# read connection parameters
params = config()

# connect to the PostgreSQL server
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(**params)

#
#
# conn = psycopg2.connect(
#     host="localhost",
#     database="task",
#     user="postgres",
#     password="123")


# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
id_student = int(input("Введите ID студента:"))

SQL_GET_TASK_BY_STUDENT = f"""SELECT  s.surname, t.name, t.condition
                                FROM  student s, student_task st,  task t
                               WHERE  s.id = st.id_student
                                 AND  st.id_task = t.id
                                 AND  s.id = {id_student}"""

cur.execute(SQL_GET_TASK_BY_STUDENT)


records = cur.fetchall()

for row in records:
    print(row)

conn.close()







