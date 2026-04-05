from fastapi import FastAPI
from auto_ppt_agent.agent import run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server running"}

@app.get("/generate-ppt")
def generate(topic: str):
    file_path = run(topic)
    return {"ppt_file": file_path}