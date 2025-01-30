from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def get_info():
    return {
        "email": "jackndiritu97@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/jackmarley254/hng12-backend-task"
    }
