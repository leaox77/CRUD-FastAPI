from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()

# Configuration for serving static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# File to store the data
DATA_FILE = "data.json"

# Load data from JSON file
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

# Read data from the JSON file
def read_data():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Save data to the JSON file
def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Root path
@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

# Root to get all items
@app.get("/items/")
async def get_items():
    data = read_data()
    return JSONResponse(content=data)

# CREATE (POST) - Request form and files
@app.post("/items/")
async def create_item(
    name: str = Form(...),
    lastname: str = Form(...),
    file: UploadFile = File(...),
):
    data = read_data()

    # Create a new item
    new_item = {
        "id": max(map(lambda x: x['id'], data)) + 1,
        "name": name,
        "lastname": lastname,
        "file": file.filename
    }
    data.append(new_item)
    write_data(data)
    return JSONResponse(content=new_item)

# UPDATE (PATCH) - Update an existing item
@app.patch("/items/{item_id}/")
async def update_item(
    item_id: int,
    item: dict,
):
    data = read_data()

    # Search for the item to update
    for existing_item in data:
        if existing_item["id"] == item_id:
            existing_item.update(item)
            write_data(data)
            return JSONResponse(content=existing_item)
    
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE (DELETE) - Delete an existing item
@app.delete("/items/{item_id}/")
async def delete_item(item_id: int):
    data = read_data()

    # Filter the item to delete
    new_data = list(filter(lambda item: item["id"] != item_id, data))
    
    if len(data) == len(new_data):
        raise HTTPException(status_code=404, detail="Item not found")

    write_data(new_data)
    return JSONResponse(content={"detail": "Item deleted"})

