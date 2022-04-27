import mysql.connector
import csv

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='<username>',
        password='<password>',
        host='<host>',
        port='3306',
        database='<database>')
    except Exception as error:
            print("Error while connecting to database for job tracker", error)
    return connection

def load_third_party(connection, file_path_csv):
    cursor = connection.cursor()
    # [Iterate through the CSV file and execute insert statement]
    cursor.execute("CREATE TABLE ticket_sales(ticket_id INT, trans_date DATE, event_id INT, event_name VARCHAR(50), event_date DATE, event_type VARCHAR(10), event_city VARCHAR(20), customer_id INT, price DECIMAL, num_tickets INT)")
    with open(file_path_csv, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            sql = 'INSERT INTO ticket_sales VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, row)
    connection.commit()
    cursor.close()
    return

def query_popular_tickets(connection):
    # Get the most popular ticket in the past month
    sql_statement = "SELECT * FROM ticket_system.ticket_sales ORDER BY num_tickets DESC LIMIT 3"
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

def main():
    file_path_csv = "third_party_sales_1.csv"
    connection = get_db_connection()
    load_third_party(connection, file_path_csv)
    records = query_popular_tickets(connection)
    with open('output.txt', 'w') as f:
        f.write("Here are the most popular tickets in the past month:\n")
        for row in records:
            f.write("- " + row[3] + "\n")

if __name__ == '__main__':
    main()