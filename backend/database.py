import sqlite3

def get_db_connection():
    conn = sqlite3.connect('talents.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS talents (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            max_rank INTEGER NOT NULL,
            current_rank INTEGER DEFAULT 0  -- Make sure this line is here!
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database cabinet created with Raw SQL!")