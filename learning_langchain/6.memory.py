from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

llm = OpenAI(temperature=0)
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

# ループで標準入力を受け付ける
while True:
    user_message = input("You: ")
    ai_message = conversation.predict(input=user_message)
    print(ai_message)
