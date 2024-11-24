import openai

# 导入 load_terminology_dictionary
from utils.intention_detector import load_terminology_dictionary


def standardize_query(query):
    """
    标准化用户的查询，将非标准化词语转换为标准化术语。
    结合大模型进一步处理语句结构，使其适合数据库查询。

    参数:
    - query (str): 用户的原始查询。

    返回:
    - str: 标准化后的查询。
    """
    # 加载术语词典
    terminology_dict = load_terminology_dictionary()

    # 1. 根据词典进行初步替换
    for term, standard in terminology_dict.items():
        if term in query:
            query = query.replace(term, standard)

    # 2. 使用大模型进一步优化和标准化 query
    prompt = f"""
    你是一个智能助手，帮助将用户的查询标准化以便于数据库查询。请将以下用户查询转换为标准化的数据库查询形式：

    原始查询: "{query}"

    标准化查询:
    """

    try:
        # 使用 OpenAI 大模型生成标准化查询
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.2
        )

        # 获取模型返回的标准化查询
        standardized_query = response.choices[0].text.strip()
        return standardized_query

    except openai.error.OpenAIError as e:
        print(f"标准化处理失败: {e}")
        return query  # 如果出错，返回初步替换后的 query


