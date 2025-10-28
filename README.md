## 📚 Library Management System (FastAPI + JSON CRUD)

A simple FastAPI project that performs **Create, Read, Update, and Delete (CRUD)** operations on a JSON file — no database needed!
Perfect for beginners learning **FastAPI**, **APIs**, and **basic backend concepts**.

---

### 🚀 Features

* 🟢 **Add new records** (books)
* 🔵 **Read all data**
* 🟠 **Update existing records**
* 🔴 **Delete records**
* 💾 Data is stored in a simple `data.json` file
* 🌐 Interactive Swagger UI for testing endpoints

---

### 🛠️ Tech Stack

* **FastAPI** — modern Python web framework
* **Uvicorn** — ASGI server for running the app
* **JSON** — lightweight file-based storage

---

### ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Saadjassal/FastAPI-JSON-CRUD.git
   cd fastapi-json-crud
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # (Windows)
   # or
   source venv/bin/activate  # (Mac/Linux)
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**

   ```bash
   uvicorn main:app --reload
   ```

---

### 🧭 How to Use (Swagger UI)

Once the server starts, open your browser and visit:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

There you can:

* `POST /books` → Add a new book
* `GET /books` → View all books
* `PUT /books/{id}` → Update a book
* `DELETE /books/{id}` → Delete a book

---

### 📁 Example JSON Format

```json
[
  {
    "id": 1,
    "title": "Atomic Habits",
    "author": "James Clear"
  },
  {
    "id": 2,
    "title": "The Alchemist",
    "author": "Paulo Coelho"
  }
]
```

---

###  Example Workflow

1. Add a new book using the Swagger UI
2. View all books with `GET /books`
3. Update or delete using the book’s ID
4. All changes are saved to `data.json`

---

###  Contributing

Feel free to fork this repo, make changes, and open a pull request.
Suggestions and improvements are always welcome! 

---

### 🧑‍💻 Author

**Saad Shahbaz**
📍 Pakistan
🌐 [GitHub Profile](https://github.com/Saadjassal)
