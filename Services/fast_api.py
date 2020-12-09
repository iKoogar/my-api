from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/html/{num}", response_class=HTMLResponse)
async def getHTML(num):
    f = open("Data/w" + str(num) + ".html", encoding="utf8")
    line = f.read()
    return HTMLResponse(content=str(line), status_code=200)



