from fastapi import FastAPI
import hashlib

app = FastAPI()

@app.post("/generate_hash")
async def generate_hash(data: dict):
    text = data.get("data", "")
    if not text:
        return {"error": "No data provided"}
    
    hashed_value = hashlib.sha256(text.encode()).hexdigest()
    return {"hash": hashed_value}

