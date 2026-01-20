from database import get_db_connection


def seed_talents():
    # 1. Establish the connection to your pantry
    conn = get_db_connection()

    # 2. Complete list of all talents from your original HTML design
    # Format: (ID, Name, Max Rank, Starting Rank)
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

    print("Stocking the pantry with talents...")

    # 3. RAW SQL: Use 'INSERT OR IGNORE' so you can run this multiple times
    # without creating duplicates if the ID already exists.
    conn.executemany('''
        INSERT OR IGNORE INTO talents (id, name, max_rank, current_rank) 
        VALUES (?, ?, ?, ?)
    ''', initial_talents)

    # 4. Save changes and close the kitchen door
    conn.commit()
    conn.close()
    print("Pantry is fully stocked! Your database is ready.")


if __name__ == "__main__":
    seed_talents()