from fastapi import FastAPI
from routes.chat import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "DocuMind Enterprise Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}