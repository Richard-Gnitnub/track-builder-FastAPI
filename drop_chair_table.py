# drop_chair_table.py

from sqlalchemy import text
from sqlmodel import create_engine, Session

# Import your model if you need (not strictly necessary for the drop operation)
# from track_app.models import Chair

DATABASE_URL = "sqlite:///./my_db.db"  # Adjust to your real DB file/path
engine = create_engine(DATABASE_URL, echo=True)

def drop_chair_table():
    with Session(engine) as session:
        # Wrap the statement in text()
        session.execute(text("DROP TABLE IF EXISTS chair;"))
        session.commit()

if __name__ == "__main__":
    drop_chair_table()
    print("Chair table dropped successfully.")
