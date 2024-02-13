from fastapi import FastAPI
import uvicorn

import json

api = FastAPI()
port = 8127

@api.get("/{test}")
async def default_route(test:str="", q:str | None = None):
    d = { 1: 'test', 2: 'jdfkjklj', 3: 'jaksdfihhjnksadjkf', "route": test }
    if q != None:
        d.update({'q':q})
    return d

if __name__ == "__main__":
    uvicorn.run("elm_api:api",host="127.0.0.1",port=port,reload=True)