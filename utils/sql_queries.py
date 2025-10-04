HABITS_TABLE_CREATION = """
CREATE TABLE IF NOT EXISTS habits(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          day TEXT, power INTEGER, root INTEGER, notes TEXT
        )
"""

INSERT_HABIT_TABLE_ENTRIES = """
INSERT INTO habits (day,power,root,notes) VALUES (?,?,?,?)
"""

READ_HABIT_TABLE = """
SELECT * FROM habits ORDER BY day DESC
"""