import re
from utils.load_schema import extract_table_definition, extract_key_terms, extract_table_descriptions_with_names
import openai
from models.llm_wrapper import  LLM

def detect_intention(query):
    """
    检测用户查询的意图，识别出可能相关的表。

    参数:
    - query (str): 用户的查询文本。

    返回:
    - list: 相关表的名称列表。
    """
    matched_tables = set()
    llm = LLM()

    table_desc_text = extract_table_definition()

    prompt = f"""
你是一个房产领域的智能助手，你需要判断用户提出的问题跟哪些房产数据库表相关联。

### 每个数据库表的描述
{table_desc_text}

### 用户的查询
{query}

请列出与该查询最相关的表的名称，以逗号分隔。如果查询与多个表相关，请确保列出所有相关表。 如果没有找到所需要的所有的
表格，输出"无"

相关表：
"""

    response = llm.query(prompt)
    # print(f"【debug】相关表【raw_response】：{response}")

    # 获取并处理模型返回的相关表列表
    related_tables = response.strip()

    # 分割返回的表名，去除空格
    related_tables_list = [table.strip() for table in related_tables.split(",") if table.strip()]
    return related_tables_list

    # try:
    #     response = llm.query(prompt)
    #
    #     # 获取并处理模型返回的相关表列表
    #     related_tables = response.strip()
    #
    #     # 分割返回的表名，去除空格
    #     related_tables_list = [table.strip() for table in related_tables.split(",") if table.strip()]
    #     return related_tables_list
    #
    # except openai.error.OpenAIError as e:
    #     print(f"意图检测失败: {e}")
    #     return []  # 如果出错，返回空列表

    # 输出匹配的表和对应描述
    print("匹配的表和描述:")
    for table in matched_tables:
        print(f"{table}: {table_descriptions.get(table)}")

    return list(matched_tables)


if __name__ == "__main__":
    print (detect_intention("这只笔多少钱?"))

