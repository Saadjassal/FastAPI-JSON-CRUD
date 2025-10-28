from fastapi import FastAPI, Body
import json
import os



app = FastAPI()
Data_file = "data.json"

#-----Helper Functions-----
# For Reading Data form Json File
def read_data():
    if not os.path.exists(Data_file):
        with open(Data_file, "w") as f:
            json.dump([], f)
    with open(Data_file, "r") as f:
        return json.load(f)
    
# for Writing Data to Json file
def write_data(data):
    with open(Data_file, "w") as f:
        json.dump(data, f, indent=4)
        
#-----Routes-----
@app.get("/")
def root():
    return {"message": "FastAPI Library Management System"}

@app.post("/books")
def add_book(book: dict = Body(...)):
    data = read_data()
    
    #Duplicate id check:
    for existing_id in data:
        if existing_id.get("id") == book.get("id"):
            return {"error": f"Book with Id {book['id']} already exists"}
        
    data.append(book)
    write_data(data)
    return {"Message": "book added successfully", "book": book}

@app.get("/books")
def get_books():
    data = read_data()
    return {"Books": data}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    data = read_data()
    for book in data:
        if book.get("id") == book_id:
            return {"Book": book}
    return {"error": "Book not found"}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict = Body(...)):
    data = read_data()
    
    for index, book in enumerate(data):
        if book.get("id") == book_id:
            data[index].update(updated_book)
            write_data(data)
            return {"message" : "Book updated successfully","Book": data[index]}
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    data = read_data()
    for book in data:
        if book.get("id") == book_id:
            data.remove(book)
            write_data(data)
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}