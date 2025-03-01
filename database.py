from dotenv import load_dotenv # type: ignore
import os
from sqlalchemy import create_engine, text


load_dotenv("connection.env")

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not found. Check your connection.env file.")

engine = create_engine(DATABASE_URL)


def load_drives():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM drives"))
        drives = []
        for row in result:
            drives.append(dict(row._mapping))
        return drives