print("app.py loaded successfully")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent_setup import run_agent

# Initialize FastAPI
app = FastAPI(title="AI Calculator API")

# Enable CORS so Streamlit (frontend) can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to ["http://localhost:8501"] if you prefer
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class Query(BaseModel):
    question: str

@app.get("/")
def read_root():
    """Root endpoint to check if API is running."""
    return {"message": "AI Calculator API is running"}

@app.post("/calculate")
def calculate(query: Query):
    """Endpoint to run the calculator agent."""
    if not query.question.strip():
        return {"error": "Empty question"}
    try:
        result = run_agent(query.question)
        return {"query": query.question, "response": result}
    except Exception as e:
        return {"error": str(e)}
