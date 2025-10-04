# helper.py
from pathlib import Path
import sqlite3, pandas as pd

from utils.sql_queries import HABITS_TABLE_CREATION, INSERT_HABIT_TABLE_ENTRIES, READ_HABIT_TABLE

DB_PATH = Path(__file__).resolve().parent.parent / "habits.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_conn() as conn:
        conn.execute(HABITS_TABLE_CREATION)

def add_entry(day, power, root, notes):
    with get_conn() as conn:
        conn.execute(INSERT_HABIT_TABLE_ENTRIES,
                     (day, power, root, notes))

def get_entries_df():
    with get_conn() as conn:
        return pd.read_sql_query(READ_HABIT_TABLE, conn)
