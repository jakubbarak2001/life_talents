from fastapi import FastAPI, HTTPException
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


@app.patch("/api/talents/{talent_id}")
def update_talent_rank(talent_id: str):
    """
    Increment a talent's current_rank by 1, up to its max_rank.
    Returns the updated talent record.
    """
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM talents WHERE id = ?", (talent_id,))
    row = cursor.fetchone()

    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Talent not found")

    current_rank = row["current_rank"]
    max_rank = row["max_rank"]

    if current_rank < max_rank:
        current_rank += 1
        conn.execute(
            "UPDATE talents SET current_rank = ? WHERE id = ?",
            (current_rank, talent_id),
        )
        conn.commit()

    updated = {
        "id": talent_id,
        "name": row["name"],
        "max_rank": max_rank,
        "current_rank": current_rank,
    }

    conn.close()
    return updated
