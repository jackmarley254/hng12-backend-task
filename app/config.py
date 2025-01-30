import os

class Config:
    EMAIL = os.getenv("EMAIL", "your-email@example.com")
    GITHUB_URL = os.getenv("GITHUB_URL", "https://github.com/yourusername/hng12-backend-task")
