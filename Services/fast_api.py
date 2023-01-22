from fastapi import FastAPI
from fastapi.responses import FileResponse
import os, random

# from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/BDD_background.png")
async def BDD_background():
    random_file_name = random.choice(os.listdir("Data/BDD_images"))
    return FileResponse("Data/BDD_images/" + random_file_name)

@app.get("/BDD_background")
async def BDD_background():
    random_file_name = random.choice(os.listdir("Data/BDD_images"))
    return FileResponse("Data/BDD_images/" + random_file_name)

@app.get("/aoba")
async def BDD_background():
    return FileResponse("Data/BDD_images/29ukLNL.png")
