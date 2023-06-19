from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates/index.html")

class Message(BaseModel):
    text: str

@app.post("/chatbot")
async def chatbot_endpoint(request: Request, message: Message):
    user_input = message.text
    response = generate_response(user_input)  # Replace this with your chatbot logic
    return {"message": response}

def generate_response(user_input):
    # Replace this with your chatbot logic to generate a response based on user input
    # Return the generated response
    return "Hello! I am a chatbot."

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("chatbot.html", {"request": request})

