from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def get_info():
    return {
        "email": "your-email@example.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/yourusername/hng12-backend-task"
    }
