import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def get_info():
    return {
        "email": "jackndiritu97@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/jackmarley254/hng12-backend-task"
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT not set
    uvicorn.run(app, host="0.0.0.0", port=port)