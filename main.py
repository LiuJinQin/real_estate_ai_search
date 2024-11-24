from handlers.query_handler import handle_query
from config.config import Config

from handlers.query_handler import handle_query

def main():

    """
        while True:
        user_input = input("用户: ")
        if user_input.lower() in ["退出", "再见"]:
            print("中介: 感谢您的咨询，期待再次为您服务！")
            break
        response = handle_query(user_input)
        print("中介:", response)

    """
    # 文件名
    # file_name = "test/questions.txt"
    # file_name = "test/questions_2类.txt"
    file_name = "test/questions_2类_subset.txt"
    # file_name = "test/questions_3类.txt"
    file_name = "test/questions_3类_预处理.txt"
    # file_name = "test/第4类问题_questions_中文.txt"
    file_name = "test/questions_2类+3类_by_sam.txt"
    file_name = "test/questions_2类_by_llm.txt"
    file_name = "test/questions_4类.txt"
    file_name = "test/questions_3类_by_llm.txt"

    # 打开文件并逐行读取
    with open(file_name, "r", encoding="utf-8") as file:
        queries = file.readlines()

    # 去掉每行的换行符并打印
    queries = [query.strip() for query in queries if query.strip() and "#" not in query]
    for i, query in enumerate(queries[:30], start=1):
        # print(f"# Q{i} - {query}")
        print(f"*********************************")
        print(f"问题序号：{i}")
        response = handle_query(query)

if __name__ == "__main__":
    main()
