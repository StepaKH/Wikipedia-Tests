import hashlib
from datetime import datetime

import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()
fake_db = {
    "commits": [],
    "releases": [],
    "webhooks": []
}

# Имитация GitHub API
@app.post("/repos/{owner}/{repo}/git/commits")
async def create_commit(owner: str, repo: str, payload: dict):
    commit_id = hashlib.sha1(str(datetime.now()).encode()).hexdigest()[:7]
    fake_db["commits"].append({
        "id": commit_id,
        "message": payload.get("message", "No commit message"),
        "timestamp": datetime.now().isoformat()
    })
    return JSONResponse({
        "sha": commit_id,
        "html_url": f"http://github.com/{owner}/{repo}/commit/{commit_id}"
    })

# Эндпоинт для вебхуков
@app.post("/api/webhook")
async def handle_webhook(request: Request):
    event = request.headers.get("X-GitHub-Event", "push")
    payload = await request.json()

    if event == "push":
        fake_db["webhooks"].append(payload)
        return {"status": "webhook_received"}

    raise HTTPException(400, "Unsupported event type")

# Запуск сервера
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)