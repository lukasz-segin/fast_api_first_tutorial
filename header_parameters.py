from typing import Optional, List

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/imputs/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}


@app.get("/users1/")
async def read_items(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token": x_token}
