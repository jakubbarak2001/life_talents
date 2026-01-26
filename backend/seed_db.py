from database import get_db_connection, create_tables


def seed_talents():
    create_tables()  # ensure the table exists (no-op if it already does)
    conn = get_db_connection()

    initial_talents = [
        # Row 1
        ('t1-1', 'Improved Vocabulary', 5, 0),
        ('t1-2', 'The Habit Loop', 3, 0),
        ('t1-3', 'Mental Declutter', 5, 0),
        ('t1-4', 'Anxiety Buffer', 3, 0),

        # Row 2
        ('t2-1', 'Emotional Processing', 3, 0),
        ('t2-2', 'Cognitive RAM', 3, 0),
        ('t2-3', 'Problem Solver', 3, 0),
        ('t2-4', 'Narrative Resilience', 1, 0),

        # Row 3
        ('t3-1', 'Pattern Seeker', 3, 0),
        ('t3-2', 'Gratitude Resilience', 1, 0),

        # Row 4
        ('t4-1', 'Insight Synthesis', 2, 0),
        ('t4-2', 'Trauma Integration', 5, 0),
        ('t4-4', 'Perspective Shift', 3, 0),

        # Row 5
        ('t5-1', 'Mindful Awareness', 2, 0),

        # Row 6
        ('t6-2', 'Architect of the Ascended Self', 1, 0)
    ]

    print("Stocking the database with talents...")

    conn.executemany('''
        INSERT INTO talents (id, name, max_rank, current_rank) 
        VALUES (?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET name=excluded.name, max_rank=excluded.max_rank
    ''', initial_talents)

    conn.commit()
    conn.close()
    print("Database is fully stocked! Your database is ready.")


if __name__ == "__main__":
    seed_talents()