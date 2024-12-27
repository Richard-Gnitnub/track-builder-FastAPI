# drop_all_tables.py

from sqlmodel import SQLModel, create_engine
# Import your models if needed, for instance:
# from track_app.models import Chair, Track, Timber

DATABASE_URL = "sqlite:///database.db"  # Must match Alembic’s DB config
engine = create_engine(DATABASE_URL, echo=True)

def drop_all_tables():
    SQLModel.metadata.drop_all(engine)
    print("All tables dropped successfully.")

if __name__ == "__main__":
    drop_all_tables()
