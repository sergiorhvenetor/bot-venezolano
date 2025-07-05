from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Cargar variables de entorno
load_dotenv()

# Inicializar el modelo (puede ser Cohere u otro)
model = init_chat_model("command-r-plus", model_provider="cohere")

# Crear la aplicación FastAPI
app = FastAPI()

# Mensaje del sistema: ¡Solo venezolano y de Venezuela!
messages = [
    SystemMessage(
        content="¡Habla únicamente en español venezolano, mi pana! "
        "Eres un experto en la cultura, gastronomía, música, historia y costumbres de Venezuela. "
        "Debes responder **solo** sobre temas venezolanos y usar modismos criollos como '¡Épale!', '¿Qué más?', 'Chamo', 'Vergatario', etc. "
        "Si te preguntan algo que no sea de Venezuela, responde con humor venezolano: '¡Nojoda, chamo, eso no es de aquí! Habla de arepas, de la Salsa Brava o de Simón Bolívar'. "
        "Tu misión es difundir la cultura venezolana con orgullo y sabor. ¡A echar vaina!"
    ),
]

@app.get("/")
async def root():
    return {"message": "¡Bienvenido a la API del Chatbot Venezolano, chamo! ¿Qué más?"}

class UserQuery(BaseModel):
    query: str

@app.post("/chat/")
async def chat(user_query: UserQuery):
    try:
        user_message = HumanMessage(content=user_query.query)
        messages.append(user_message)
        response = model.invoke(messages)
        assistant_message = AIMessage(content=response.content)
        messages.append(assistant_message)
        return {"response": assistant_message.content}
    except Exception as e:
        return {"error": f"¡Ay, chamo, algo salió mal! {str(e)}"}