# real_estate_ai_search

## 运行

1. **安装依赖**

   首先，确保你已经安装了项目所需的依赖。你可以通过以下命令安装：

   ```bash
   pip install -r requirements.txt
   ```

   这将会安装 `requirements.txt` 文件中列出的所有依赖包。

2. **配置环境变量**

   进入 `config` 文件夹，创建或编辑 `.env` 文件，输入你的 OpenAI API 密钥。使用以下命令进入该文件夹：

   ```bash
   cd config
   ```

   然后，使用 `nano` 或任何文本编辑器打开 `.env` 文件：

   ```bash
   nano .env
   ```

   在 `.env` 文件中输入你的 `OPENAI_API_KEY`：

   ```bash
   OPENAI_API_KEY='your_openai_api_key_here'
   ```

   按 `Ctrl + O` 保存文件，接着按 `Enter` 确认保存。然后按 `Ctrl + X` 退出编辑器。

3. **启动前端界面**

   配置完 `.env` 文件后，返回项目的根目录，并启动前端界面：

   ```bash
   cd ..
   python ui.py
   ```

   这将启动前端界面，你可以在浏览器中访问该界面进行操作。