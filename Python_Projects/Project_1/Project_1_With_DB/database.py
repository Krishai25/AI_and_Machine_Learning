import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database="student",
        cursorclass=pymysql.cursors.DictCursor
    )
def insert_students(stud_id,name,classname,marks):
    conn = get_connection()
    try :
       with conn.cursor() as cursor:
          query = """
          INSERT INTO student_report(stud_id,name,classname,ai,web_mining,comp_networks,os,ml)
          Values(%s,%s,%s,%s,%s,%s,%s,%s)
          """
          cursor.execute(query,(stud_id,name,classname,*marks))
          conn.commit()
          print(f"✅ Student {name} inserted into DB")
          conn.close()
    except Exception as e:
        print("Connection Not Established -> ",e )

def fetch_students(stud_id):
    conn = get_connection()
    try :
       with conn.cursor() as cursor:
          query = """
          Select * from student_report where stud_id=%s
          """
          cursor.execute(query,(stud_id,))
          row=cursor.fetchone()
          conn.commit()
          conn.close()
          return row
    except Exception as e:
        print("Connection Not Established -> ",e )
def fetch_all_students():
    conn = get_connection()
    try :
       with conn.cursor() as cursor:
          query = """
          select * from student_report
          """
          cursor.execute(query)
          row=cursor.fetchall()
          conn.commit()
          conn.close()
          return row
    except Exception as e:
        print("Connection Not Established -> ",e )

def update_grade_percentage(stud_id, total, percentage, grade):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE student_report
        SET total = %s, percentage = %s, grade = %s
        WHERE stud_id = %s
    """
    cursor.execute(query, (total, percentage, grade, stud_id))
    conn.commit()
    print(f"✅ Grade & Percentage updated for {stud_id}")
    cursor.close()
    conn.close()

