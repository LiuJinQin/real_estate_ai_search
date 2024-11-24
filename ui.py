
import gradio as gr
from handlers.query_handler import handle_query


# 文件名
# file_name = "test/questions_2类_subset.txt"
# file_name = "test/questions_3类_预处理.txt"
# file_name = "test/第4类问题_questions_中文.txt"
file_name = "test/questions_all(234sam+23llm)_for_ui.txt"

# 打开文件并逐行读取
with open(file_name, "r", encoding="utf-8") as file:
    queries = file.readlines()

# 去掉每行的换行符并打印
queries = [query.strip() for query in queries if query.strip() and "#" not in query]

def text_to_sql(user_input, chat_history):

    # 打印输入
    # print(f"用户输入：{user_input}")  # 是否有100万到200万之间的房源推荐？
    # print(f"初始聊天记录：{chat_history}")  # []

    # 获取 AI 回复
    ai_reply = handle_query(user_input)

    # 处理返回
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": ai_reply})

    return "", chat_history

def text_to_sql_good_display_sql_code(user_input, chat_history):

    # 打印输入
    # print(f"用户输入：{user_input}")  # 是否有100万到200万之间的房源推荐？
    # print(f"初始聊天记录：{chat_history}")  # []

    # 获取 AI 回复
    ai_reply = handle_query(user_input)
    ai_reply = f"""生成的SQL：
```sql{ai_reply}
```
"""

    # 处理返回
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": ai_reply})

    return "", chat_history
    

with gr.Blocks() as demo:
    gr.Markdown("### 后花园 AI Search")
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                label="AI 中介助手",
                type="messages",
            )
            user_input = gr.Textbox(
                label="User Question",
                placeholder="请输入您的问题",
                value=queries[0]
            )
            user_input.submit(
                fn=text_to_sql_good_display_sql_code,
                inputs=[user_input, chatbot],
                outputs=[user_input, chatbot]
            )
            submit_btn = gr.Button("Search")
            submit_btn.click(
                fn=text_to_sql_good_display_sql_code,
                inputs=[user_input, chatbot],
                outputs=[user_input, chatbot]
            )
            clear_btn = gr.ClearButton([user_input, chatbot])
        with gr.Column(scale=2):
            with gr.Tab("示例用户问题"):
                example_user_inputs = gr.JSON(queries)
demo.launch(debug=True)