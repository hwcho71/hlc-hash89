import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running!"}

PORT = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
