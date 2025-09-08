# 🤖 User-Data-Fetch-Agent

An async-powered AI agent built with the Gemini 2.0 Flash model, capable of invoking tools and fetching external data via APIs. This project demonstrates how to integrate OpenAI-style agents with custom toolchains and run them using an event-driven architecture.

## 🚀 Features

- Async agent execution using `asyncio`
- Tool invocation via `@function_tool` decorator
- External API integration (`jsonplaceholder.typicode.com`)
- Gemini 2.0 Flash model support
- Environment-based configuration with `.env`

## 🧠 How It Works

The agent is initialized with:
- A name and instruction set
- A tool (`fetch_user_data`) that retrieves user data from an external API
- A model (`OpenAIChatCompletionsModel`) powered by Gemini

When the agent receives input like `"Please fetch and show me the list of user names with their ID."`, it intelligently decides to invoke the tool and return the result.

## 🛠️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/gemini-agent-toolkit.git
cd gemini-agent-toolkit
 ```
### 2.  **Install dependencies:**

    **Using pip:**

    ```bash
    pip install -r requirements.txt
    ```

### 3.  **Create .env File**

    ```Env
    GEMINI_API_KEY=your_api_key_here
    base_url=https://your-gemini-endpoint.com
    ```

### 4. **Run the Agent**

    ```Bash
     python main.py
    ```
## 👨‍💻 Author
Kaif Shamim Crafted with curiosity and code.
