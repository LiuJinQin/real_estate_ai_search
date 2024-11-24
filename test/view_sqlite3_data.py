import sqlite3

def view_database(db_path):
    try:
        # 连接到数据库
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 获取所有表名
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("数据库中的表：")
        for table in tables:
            print(f"- {table[0]}")

        # 遍历每个表并显示所有数据
        for table in tables:
            table_name = table[0]
            print(f"\n表 {table_name} 的数据：")
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            # 获取列名
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = [info[1] for info in cursor.fetchall()]
            print(f"列名: {columns}")

            # 打印数据
            for row in rows:
                print(row)

        # 关闭连接
        conn.close()

    except sqlite3.Error as e:
        print(f"数据库操作失败: {e}")

# 指定数据库路径
db_path = "../data/real_estate.db"
view_database(db_path)
