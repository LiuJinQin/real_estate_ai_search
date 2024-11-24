from pathlib import Path
import re

# 全局变量用于缓存 schema 内容
SCHEMA_TABLE_FIELD_DEFINITION = None   # 存放每个表的描述和字段描述，用于textsql
SCHEMA_TABLE_DEFINITION = None       # 存放每个表的描述，用于意图识别
KEY_TERMS = None  # 关键词库以及解释，用于query的标准化

def extract_table_definition():
    """
    从文件中加载数据库表结构定义，将每个表结构存储在字典中并缓存到内存中。

    返回:
    - dict: 包含每个表结构的字典，表名为键，表结构描述为值。
    """
    global SCHEMA_TABLE_FIELD_DEFINITION
    if SCHEMA_TABLE_FIELD_DEFINITION is None:
        # 初始化缓存字典
        SCHEMA_TABLE_FIELD_DEFINITION = {}

        # 定义文件路径
        file_path = Path(__file__).resolve().parent.parent / 'config' / 'schema_definition.txt'
        file_path = Path(__file__).resolve().parent.parent / 'config' / 'database_schema_definition_v1.txt'

        # 定义正则表达式模式，用于匹配表名和描述信息
        table_pattern = re.compile(r"## 表：(\w+)")
        description_pattern = re.compile(r"- 描述：(.*)")

        # 读取文件内容并解析
        with file_path.open('r', encoding='utf-8') as file:
            lines = file.readlines()

        current_table = None
        current_structure = []

        for line in lines:
            # 查找表名称
            table_match = table_pattern.match(line)
            if table_match:
                # 如果当前表结构已存在，保存至缓存字典
                if current_table and current_structure:
                    SCHEMA_TABLE_FIELD_DEFINITION[current_table] = "\n".join(current_structure)

                # 更新当前表名，重置结构缓存
                current_table = table_match.group(1)
                current_structure = [line.strip()]  # 初始化为包含表名的结构行
                continue

            # 将表结构行添加到当前表的结构中
            if current_table:
                current_structure.append(line.strip())

        # 处理最后一个表结构
        if current_table and current_structure:
            SCHEMA_TABLE_FIELD_DEFINITION[current_table] = "\n".join(current_structure)

    return SCHEMA_TABLE_FIELD_DEFINITION


def extract_table_descriptions_with_names():
    """
    从 schema_definition.txt 文件中提取每个表的名称和描述信息，并格式化为 "表名：描述"。

    返回:
    - str: 每个表的名称和描述信息字符串，不同表用换行符分隔，每行格式为 "表名：描述"。
    """
    global SCHEMA_TABLE_DEFINITION

    if SCHEMA_TABLE_DEFINITION is None:

        # 定义文件路径
        file_path = Path(__file__).resolve().parent.parent / 'config' / 'schema_definition.txt'

        # 定义正则表达式模式
        table_pattern = re.compile(r"## 表：(\w+)")
        description_pattern = re.compile(r"- 描述：(.*)")

        descriptions = []

        # 读取文件内容并解析
        with file_path.open('r', encoding='utf-8') as file:
            lines = file.readlines()

        current_table = None

        for line in lines:
            # 查找表名称
            table_match = table_pattern.match(line)
            if table_match:
                current_table = table_match.group(1)  # 获取表名
                continue

            # 查找描述信息
            description_match = description_pattern.search(line)
            if description_match and current_table:
                # 将表名和描述格式化为 "表名：描述" 并添加到列表
                descriptions.append(f"{current_table}：{description_match.group(1)}")
                current_table = None  # 重置表名

        # 使用换行分隔每个表的名称和描述
        SCHEMA_TABLE_DEFINITION = "\n".join(descriptions)

        return SCHEMA_TABLE_DEFINITION
def extract_key_terms():
    global KEY_TERMS

    if KEY_TERMS is None:
        # 定义文件路径
        file_path = Path(__file__).resolve().parent.parent / 'config' / 'key_terms.txt'

        # 读取文件内容为一个字符串
        with file_path.open("r", encoding="utf-8") as file:
            KEY_TERMS = file.read()

        return KEY_TERMS


if __name__ == "__main__":
    print (extract_table_definition())
    print (extract_table_descriptions_with_names())
    print (extract_key_terms())