from fastapi import FastAPI, HTTPException
import hashlib

app = FastAPI()

@app.get("/")  # Root endpoint to test if API is running
def home():
    return {"message": "API is running!"}

@app.post("/generate_hash")  # Fix this route to ensure it's working
async def generate_hash(data: dict):
    text = data.get("data", "")
    if not text:
        raise HTTPException(status_code=400, detail="No data provided")

    hashed_value = hashlib.sha256(text.encode()).hexdigest()
    return {"hash": hashed_value}
