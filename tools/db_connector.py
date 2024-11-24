from sqlalchemy import create_engine
from config.config import Config
import sqlite3

class DatabaseConnector:

    def __init__(self):
        # 连接数据库
        self.conn = sqlite3.connect('data/real_estate.db')
        self.cursor = self.conn.cursor()

    def query(self, sql_query):
        # 执行查询
        self.cursor.execute(str(sql_query))
        results = self.cursor.fetchall()

        # 打印结果
        for row in results:
            print(row)

        # 关闭连接
        self.conn.close()

        print(results)

if __name__ == "__main__":

    dbconn = DatabaseConnector()
    dbconn.query("SELECT *FROM properties WHERE suburb = 'Remuera' AND pricing_method = '拍卖' AND listing_date >= DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY);")
