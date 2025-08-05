from langchain_ollama.llms import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from tools import review_tool

# Load LLM
llm = OllamaLLM(model="llama3.2")

# Initialize agent with the tool
agent = initialize_agent(
    tools=[review_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# CLI loop
while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question.lower() == "q":
        break

    # Agent decides what to do
    response = agent.run(question)
    print(response)
