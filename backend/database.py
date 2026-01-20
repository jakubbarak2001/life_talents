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


def seed_data():
    conn = get_db_connection()
    # A list of our initial talents
    initial_talents = [
        ('t1-1', 'Improved Vocabulary', 5),
        ('t1-2', 'The Habit Loop', 3),
        ('t1-3', 'Mental Declutter', 5),
        ('t1-4', 'Anxiety Buffer', 3)
    ]

    # RAW SQL: "Insert this data, but if the ID already exists, do nothing"
    conn.executemany('''
        INSERT OR IGNORE INTO talents (id, name, max_rank) 
        VALUES (?, ?, ?)
    ''', initial_talents)

    conn.commit()
    conn.close()
    print("Pantry filled with initial talents!")


if __name__ == "__main__":
    create_tables()
    seed_data()