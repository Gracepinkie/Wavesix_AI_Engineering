import os
from openai import OpenAI
from dotenv import load_dotenv
from tools import add, subtract, multiply, divide, show_history

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a calculator assistant that can use the following functions:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)
- show_history()

When answering, always follow this format:
Thought: ...
Action: function_call()
Observation: ...
Final Answer: ...
"""

def run_agent(user_input: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )

    reply = response.choices[0].message.content
    print(f"\n🧠 Agent:\n{reply}")

    if "Action:" in reply:
        try:
            action_line = [line for line in reply.splitlines() if line.startswith("Action:")][0]
            action_code = action_line.replace("Action:", "").strip()
            print(f"\n⚙️ Running: {action_code}")
            result = eval(action_code, globals())
            return f"Final Answer: {result}"
        except Exception as e:
            return f"❌ Eval Error: {e}"
    return reply
