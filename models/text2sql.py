import openai
from utils.intention_detector import detect_intention
from utils.load_schema import extract_table_definition
from models.llm_wrapper import LLM
from sqlalchemy import text
import re


def filter_schema(related_tables):
    """
    根据给定的表名，抽取相关表的描述和字段描述。

    参数：
    - related_tables(list)：list of 表明

    返回：
    - str: 表的描述和字段描述，作为大模型调用的上下文。
    """
    schema_content = extract_table_definition()
    extracted_info = []

    for table in related_tables:
        if table in schema_content:
            table_info = schema_content[table]
            # 格式化输出，每个表的内容开头带 "## 表" 以保持结构一致
            extracted_info.append(f"{table_info.strip()}")

    return "\n\n".join(extracted_info)

def extract_sql_code(raw_response):
    """
    从字符串中提取 ```sql 和 ``` 之间的 SQL 代码。

    参数:
        raw_response (str): 包含 SQL 代码的字符串。

    返回:
        str: 提取出的 SQL 代码。如果未找到，返回空字符串。
    """
    try:
        # 使用正则表达式提取 ```sql 和 ``` 之间的内容
        match = re.search(r"```sql(.*?)```", raw_response, re.DOTALL)
        if match:
            return match.group(1).strip()  # 返回去掉首尾空格的 SQL 代码
        else:
            return ""  # 未找到时返回空字符串
    except Exception as e:
        return f"Error extracting SQL: {str(e)}"

def text_to_sql(question, related_tables):
    schema_definition = filter_schema(related_tables)
    #print (schema_definition)
    # prompt = f"""
    # 你是一个智能的房产领域SQLite助手。 把用户的问题转换为SQLite语句。 下面是房产数据库的表结构定义：
    #
    # {schema_definition}
    #
    # 根据上述表结构，请为以下问题生成一个 SQLite 查询：
    #
    # 问题：{question}
    #
    # SQLite 查询：
    # """
    prompt = f"""
你是一个智能的房产领域 MySQL 助手，能把用户的问题转换为 MySQL 语句。 下面是房产数据库的表结构定义：

{schema_definition}

根据上述表结构，请为以下问题生成一个 MySQL 查询：

问题：{question}

MySQL 查询：
"""
    #print ("prompt is: ", prompt)

    llm = LLM()

    response = llm.query(prompt)
    # print(f"【debug】生成的SQL【raw_response】：\n{response}")
    sql_query = extract_sql_code(response)
    return sql_query

    #
    # try:
    #     response = llm.query(prompt)
    #     response = response.replace("sql\n", "", 1).strip()
    #     response = response.strip('```')
    #
    #     #print ("获取到的sql为：\n", response)
    #     #sql_query = response.strip()
    #     return text(response)
    #
    # except openai.error.OpenAIError as e:
    #     print(f"意图检测失败: {e}")
    #     return []  # 如果出错，返回空列表