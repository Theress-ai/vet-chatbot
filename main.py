from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

app = FastAPI()

class Question(BaseModel):
    question: str

llm = ChatOpenAI(
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

@app.get("/")
def home():
    return {"message": "Veterinary chatbot is running 🐾"}

@app.post("/askbot")
async def ask_bot(q: Question):
    try:
        response = llm([HumanMessage(content=q.question)])
        return {"response": response.content}
    except Exception as e:
        return {"error": str(e)}
