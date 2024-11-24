import openai
from config.config import Config
from openai import OpenAI

class LLM:
    def __init__(self, model="gpt-4o", max_tokens=300, temperature=0.7):
        """
        初始化 OpenAI API Wrapper。

        参数:
        - model (str): 使用的模型名称，默认使用 "text-davinci-003"。
        - max_tokens (int): 返回的最大 token 数。
        - temperature (float): 控制生成文本的随机性，0.0 更确定，1.0 更随机。
        """
        # openai.api_key = Config.OPENAI_API_KEY
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def query(self, user_query, chat_history=[]):
        """
        使用给定的用户输入和对话历史，调用 OpenAI Chat API，并返回 GPT-4 的响应。

        参数:
        - user_query (str): 用户的查询文本。
        - chat_history (list): 对话历史，是一个包含字典的列表，每个字典代表一条消息。

        返回:
        - str: 模型生成的响应文本。
        """
        # 将用户的查询追加到对话历史中
        chat_history.append({"role": "user", "content": user_query})

        # try:
        #     # 使用 OpenAI Chat API 获取回复
        #     response = openai.ChatCompletion.create(
        #         model=self.model,
        #         messages=chat_history,
        #         max_tokens=self.max_tokens,
        #         temperature=self.temperature
        #     )
        #
        #     # 获取并返回模型的响应文本
        #     reply = response['choices'][0]['message']['content'].strip()
        #
        #     # 将模型的回复追加到对话历史中
        #     chat_history.append({"role": "assistant", "content": reply})
        #
        #     return reply
        # except openai.error.OpenAIError as e:
        #     print("OpenAI API 请求出错:", e)
        #     return None
        # 使用 OpenAI Chat API 获取回复
        response = self.client.chat.completions.create(
            model=self.model,
            messages=chat_history,
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )

        # 获取并返回模型的响应文本
        reply = response.choices[0].message.content.strip()

        # 将模型的回复追加到对话历史中
        chat_history.append({"role": "assistant", "content": reply})

        return reply


if __name__ == "__main__":
    llm = LLM()
    print (llm.query("利用gpt4 chat model回复用户的query，写代码"))

