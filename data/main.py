print("main.py is running")  # Add this line to verify execution

from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "API is running"}