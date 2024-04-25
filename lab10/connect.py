import psycopg2
import csv
import config

# Настройки подключения к базе данных
def connect_db():
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(
        dbname=config.DB_NAME, 
        user=config.DB_USER, 
        password=config.DB_PASSWORD, 
        host=config.DB_HOST, 
        port=config.DB_PORT
    )
    return conn

# Создание таблицы в базе данных
def create_tables(conn):
    """ create tables in the PostgreSQL database"""
    command = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone VARCHAR(255) UNIQUE NOT NULL
        );
        """
    )
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()
    cur.close()

# Вставка данных в таблицу из консоли
def insert_phonebook(conn, first_name, last_name, phone):
    """ insert a new record into the phonebook table """
    sql = """INSERT INTO phonebook(first_name, last_name, phone)
             VALUES(%s, %s, %s) RETURNING user_id;"""
    cur = conn.cursor()
    cur.execute(sql, (first_name, last_name, phone))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return user_id

# Загрузка данных из CSV файла
def upload_data_from_csv(conn, csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        for row in reader:
            insert_phonebook(conn, row[0], row[1], row[2])

# Обновление данных в таблице
def update_phonebook(conn, user_id, first_name=None, phone=None):
    """ update first name or phone of a phonebook entry """
    sql = "UPDATE phonebook SET first_name = %s, phone = %s WHERE user_id = %s"
    cur = conn.cursor()
    cur.execute(sql, (first_name, phone, user_id))
    conn.commit()
    cur.close()

# Запрос данных из таблицы с фильтрами
def query_data(conn, filter_by=None):
    """ query phonebook entries by filter """
    cur = conn.cursor()
    query = "SELECT * FROM phonebook"
    if filter_by:
        query += " WHERE " + " OR ".join([f"{key}='{value}'" for key, value in filter_by.items()])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()

# Удаление данных из таблицы
def delete_phonebook_entry(conn, first_name=None, phone=None):
    """ delete an entry in the phonebook by first name or phone """
    sql = "DELETE FROM phonebook WHERE first_name = %s OR phone = %s"
    cur = conn.cursor()
    cur.execute(sql, (first_name, phone))
    conn.commit()
    cur.close()

if __name__ == '__main__':
    conn = connect_db()
    create_tables(conn)