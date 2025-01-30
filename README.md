# HNG12 Backend Task - Public API

## Description
This is a simple API built using FastAPI that returns:
- Registered email
- Current datetime in ISO 8601 format
- GitHub repository URL

## 📌 API Documentation

### Endpoint

- **URL:** `https://hng12-api.onrender.com/`
- **Method:** `GET`
- **Response Format:** `JSON`

### Example Response

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/hng12-backend-task"
}
```

## Setup Instructions

### 1 Clone the repository

```bash
git clone https://github.com/yourusername/hng12-backend-task.git
cd hng12-backend-task
```


### 2 Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3 Install dependencies

```bash
pip install -r requirements.txt
```

### 4 Run the Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Example Usage

#### Using `curl`

```bash
curl -s https://hng12-backend-stage-zero.vercel.app
```

#### Using a browser 

1. Open  your browser.
2. Enter the API URL:
   ```
   https://hng12-backend-stage-zero.vercel.app/
   ```
3. Send a `GET` request.
4. View the JSON response

## Hire Python Developers

If you're looking to hire Python developers, check out [HNG Tech - Hire Python Developers](https://hng.tech/hire/python-developers).

## 📝 License

This project is open-source and available under the **MIT License**.

## 📢 Contact

💎 **Email:** [jackndiritu97@gmail.com](mailto:jackndiritu97@gmail.com)\
🔗 **GitHub:** [jackmarley254](https://github.com/jackmarley254)\
🔗 **LinkedIn:** [Jackson Gitahi](https://linkedin.com/in/jackson-gitahi)
