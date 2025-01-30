import os

class Config:
    EMAIL = os.getenv("EMAIL", "jackndiritu97@gmail.com")
    GITHUB_URL = os.getenv("GITHUB_URL", "https://github.com/jackmarley254/hng12-backend-task")
