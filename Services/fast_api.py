from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os, random

# from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/text")
async def BDD_background():
    return FileResponse("Data/scratch.txt")

@app.get("/pdf")
async def BDD_background():
    return FileResponse("Data/Sorting-Part_2.pdf")