import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, AIMessage

# Cargar variables de entorno
load_dotenv()

# Set Tavily API key
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# Inicializar el modelo
llm = ChatCohere(model="command-r-plus")

# Inicializar herramientas
tools = [TavilySearchResults(max_results=2)]

# Crear el prompt
# Note: The prompt template now includes a placeholder for agent_scratchpad
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can search for information."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


# Crear el agente
agent = create_react_agent(llm, tools, prompt)

# Crear el ejecutor del agente
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