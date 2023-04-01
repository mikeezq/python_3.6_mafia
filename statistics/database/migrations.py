import os

import psycopg2
import csv

from constants import TABLES_MAP

postgre_connect = psycopg2.connect(
    host="127.0.0.1",
    database="mydb",
    user="myuser",
    password="mypassword"
)


def create_tables():
    with postgre_connect as connection:
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            for table in TABLES_MAP:
                table_name = table

                query = f"""CREATE TABLE {table_name} ("""
                for column, type in TABLES_MAP[table].items():
                    query += f"""{column} {type},"""
                query = query[:-1]
                query += ");"

                try:
                    cursor.execute(query)
                except psycopg2.errors.DuplicateTable:
                    connection.rollback()
                    continue


def copy_data():
    cur_dir = os.getcwd()
    csv_files_dir = os.path.join(cur_dir, "../tabels")

    with postgre_connect as connection:
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            for table in TABLES_MAP:
                table_name = table
                columns = TABLES_MAP[table_name]
                insert = f"""INSERT INTO {table_name} ({', '.join(columns.keys())}) VALUES """

                print(f"TABLE: {table_name}")
                with open(os.path.join(csv_files_dir, table_name + ".csv"), newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile, delimiter=';')
                    next(reader)
                    format_string = f"({'%s, ' * len(columns.keys())}"
                    format_string = f"{format_string[:-2]})"
                    query = insert + format_string

                    for row in reader:
                        cursor.execute(query, row)
                        connection.commit()
