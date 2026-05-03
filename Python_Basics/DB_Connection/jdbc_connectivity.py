import pymysql

connection=pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    # Query for creating a table
    with connection.cursor() as cursor:

        create_query = """
        Create TABLE IF NOT EXISTS Employee (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(100), 
        department VARCHAR(100) 
        ); 
      """
        cursor.execute(create_query)


        insert_query = "Insert INTO Employee (name, department) VALUES (%s, %s)"
        values=[("John","IT"),("Bob","HR"),("Alice","Finance")]
        cursor.executemany(insert_query, values)
        connection.commit()

        select_query="SELECT * FROM Employee"
        cursor.execute(select_query)

        for row in cursor.fetchall():
            print(row)

finally:
    cursor.close()


