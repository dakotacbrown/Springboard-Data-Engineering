# 15.3 Data Pipeline Mini-Project

## How to run
Before running the program, you should update the `get_db_connection()` method by inputting your own mysql username, password, host, and database. After that you just need to run the program. The table is created and everything is inserted for you.

```
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
```

