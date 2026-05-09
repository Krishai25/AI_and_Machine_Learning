from database_connection_expense_tracker import get_connection

class ExpenseTrack:
    def __init__(self):
        self.conn = get_connection()
        self.cursor=self.conn.cursor()

    def add_expense(self,category_name,price):
        query ="""
        INSERT INTO expense (category,price)
        values (%s,%s)"""
        self.cursor.execute(query,(category_name,price))
        self.conn.commit()
        print("Successfully added expense")

    def get_expense_by_category(self,category_name):
        query ="""
        SELECT * from expense WHERE category = %s
        """
        self.cursor.execute(query,(category_name,))
        result = self.cursor.fetchall()
        return result

    def get_highest_expense(self):
        query ="""
        SELECT * from expense
        ORDER BY price DESC LIMIT 1
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_total_of_the_expense(self):
        query = "SELECT SUM(price) FROM expense"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

    def view_all_expense(self):
        query ="""
        SELECT * from expense
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Successfully closed")

