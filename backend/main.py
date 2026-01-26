from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_connection  # Import your new connection tool

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/talents")
def get_talents():
    # 1. Open the cabinet
    conn = get_db_connection()

    # 2. RAW SQL: "Select everything from the talents table"
    cursor = conn.execute('SELECT * FROM talents')
    rows = cursor.fetchall()
    conn.close()

    # 3. Format the data for the Dining Room
    # We turn the database rows into a dictionary the frontend understands
    talents_dict = {}
    for row in rows:
        talents_dict[row['id']] = {
            "name": row['name'],
            "max_rank": row['max_rank'],
            "current_rank": row['current_rank']
        }

    return talents_dict
