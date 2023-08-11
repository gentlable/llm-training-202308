from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
import langchain


langchain.verbose = True

chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = load_tools(["terminal"], llm=chat)
agent_executor = initialize_agent(
    tools, chat, agent="zero-shot-react-description")

result = agent_executor.run("ターミナルのエンコードをutf-8に変更してから,現在のディレクトリにあるファイルの一覧を教えてください。")
print(result)
