import sqlite3

# 假设数据库文件已存在
DATABASE_FILE = 'real_estate_demo.db'
QUESTIONS_FILE = 'questions_for_test_adjust_the_order.txt'

# 读取问题文件，执行测试
def run_tests():
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # 读取问题文件
    with open(QUESTIONS_FILE, 'r') as file:
        questions = file.readlines()

    # 对每个问题进行测试
    for question in questions:
        question = question.strip()  # 去掉行尾的换行符
        if not question:
            continue  # 跳过空行

        print(f"\n问题: {question}")
        sql_query = text_to_sql(question)

        if sql_query:
            try:
                cursor.execute(sql_query)
                result = cursor.fetchall()
                if result:
                    for row in result:
                        print("结果:", row)
                else:
                    print("结果: 未找到符合条件的记录。")
            except sqlite3.Error as e:
                print("执行SQL时出错:", e)
        else:
            print("无法识别的问题格式，未生成SQL语句。")

    # 关闭数据库连接
    conn.close()


if __name__ == "__main__":
    run_tests()