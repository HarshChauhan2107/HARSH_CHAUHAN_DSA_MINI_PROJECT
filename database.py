"""SQLite persistence layer."""
import sqlite3
from pathlib import Path

DEFAULT_DB = Path(__file__).resolve().parent / "numerology.db"


class Database:
    def __init__(self, db_path=None):
        self.db_path = str(db_path or DEFAULT_DB)
        self.initialize()

    def connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def initialize(self):
        with self.connect() as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    original_name TEXT NOT NULL,
                    normalized_name TEXT NOT NULL,
                    total INTEGER NOT NULL,
                    numerology_number INTEGER NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def create(self, record):
        with self.connect() as con:
            cursor = con.execute(
                """INSERT INTO records
                   (original_name, normalized_name, total, numerology_number)
                   VALUES (?, ?, ?, ?)""",
                (record["original_name"], record["normalized_name"],
                 record["total"], record["numerology_number"])
            )
            record_id = cursor.lastrowid
            row = con.execute("SELECT * FROM records WHERE id=?", (record_id,)).fetchone()
            return dict(row)

    def get_all(self):
        with self.connect() as con:
            rows = con.execute("SELECT * FROM records ORDER BY id ASC").fetchall()
            return [dict(row) for row in rows]

    def get(self, record_id):
        with self.connect() as con:
            row = con.execute("SELECT * FROM records WHERE id=?", (record_id,)).fetchone()
            return dict(row) if row else None

    def update(self, record_id, record):
        with self.connect() as con:
            cursor = con.execute(
                """UPDATE records SET original_name=?, normalized_name=?,
                   total=?, numerology_number=? WHERE id=?""",
                (record["original_name"], record["normalized_name"],
                 record["total"], record["numerology_number"], record_id)
            )
            return cursor.rowcount > 0

    def delete(self, record_id):
        with self.connect() as con:
            cursor = con.execute("DELETE FROM records WHERE id=?", (record_id,))
            return cursor.rowcount > 0

    def clear(self):
        with self.connect() as con:
            con.execute("DELETE FROM records")
