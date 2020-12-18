from fastapi import FastAPI
from fastapi.responses import FileResponse
import os, random

# from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

"""
@app.get("/html/{num}", response_class=HTMLResponse)
async def getHTML(num):
    f = open("Data/w" + str(num) + ".html", encoding="utf8")
    line = f.read()
    return HTMLResponse(content=str(line), status_code=200)
"""

@app.get("/BDD_background")
async def BDD_background():
    random_file_name = random.choice(os.listdir("Data/BDD_images"))
    return FileResponse("Data/BDD_images/" + random_file_name)

