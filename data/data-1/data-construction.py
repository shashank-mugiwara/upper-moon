import random
from random import randint

import psycopg2
import csv

FULL_NAMES_FILE_PATH = '''C:\\Users\\wwwsh\\Downloads\\fbnames\\fullNames\\fullnames.txt'''
ADDRESS_FILE_PATH = '''C:\\Users\\wwwsh\\Downloads\\fbnames\\fullNames\\fulladdress.csv'''

def get_db_connection():
    connection = psycopg2.connect(user="dbuser",
                                  password="root",
                                  host="localhost",
                                  port="7432",
                                  database="benchmarking")
    return connection

def insert_data(connection, first_name=None, middle_name=None, last_name=None, phone=None, address=None):
    cursor = connection.cursor()
    postgres_insert_query = """INSERT INTO individual (first_name, middle_name, last_name, phone, address) VALUES (
    %s,%s,%s, %s, %s) """
    record_to_insert = (first_name, middle_name, last_name, phone, address)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into individual table")


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

db_connection = get_db_connection()
address_data = []
with open(ADDRESS_FILE_PATH, newline='') as f:
    reader = csv.reader(f)
    address_data = list(reader)
address_data.pop()

fullnames_data = []
with open(FULL_NAMES_FILE_PATH, "r") as f:
    data = f.read()
    fullnames_data = data.split('\n')

fullnames_data = fullnames_data[:-1]
random.shuffle(fullnames_data)
for i in range(0, len(fullnames_data)):
    fullnames = fullnames_data[i]
    fullnames = fullnames.strip().split(' ')
    address = address_data[i]
    random.shuffle(address)
    address = ','.join(address)
    insert_data(connection=db_connection, first_name=fullnames[-1], middle_name=None, last_name=fullnames[-2], phone=random_with_N_digits(12), address=address)



print(len(address_data))
print(len(fullnames_data))
