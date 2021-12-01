from typing import Optional

from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}
