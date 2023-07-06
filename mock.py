# mock.py
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_item(name: str = ""):
    return {"name": name}


if __name__ == '__main__':
    uvicorn.run(
        app="mock:app",
        host=os.popen("hostname -I").read().split(" ")[0], # 自动获取本机IP
        port=5000,
        reload=True
    )
