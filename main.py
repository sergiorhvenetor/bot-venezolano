import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()

# Set Tavily API key
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# Initialize the model
llm = ChatCohere(model="command-r-plus")

# Initialize tools
tools = [TavilySearchResults(max_results=2)]

# Create the prompt
# Note: The prompt template now includes a placeholder for agent_scratchpad
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can search for information."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


# Create the agent
agent = create_react_agent(llm, tools, prompt)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def get_response(query):
    """
    Gets a response from the agent.
    """
    response = agent_executor.invoke({"input": query})
    return response["output"]

if __name__ == "__main__":
    # Example usage
    query = "What is the weather in New York?"
    response = get_response(query)
    print(response)