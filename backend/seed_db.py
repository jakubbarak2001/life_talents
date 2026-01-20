from database import get_db_connection


def seed_talents():
    conn = get_db_connection()
    initial_talents = [
        ('t1-1', 'Improved Vocabulary', 5),
        ('t1-2', 'The Habit Loop', 3),
        ('t1-3', 'Mental Declutter', 5),
        ('t1-4', 'Anxiety Buffer', 3)
    ]

    conn.executemany('''
        INSERT OR IGNORE INTO talents (id, name, max_rank) 
        VALUES (?, ?, ?)
    ''', initial_talents)

    conn.commit()
    conn.close()
    print("Database is now stocked with talents!")


if __name__ == "__main__":
    seed_talents()