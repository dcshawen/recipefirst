from fastapi import FastAPI
import db;

app = FastAPI()


@app.get("/")
async def root():
    return {"message": db.getDBSchema()}