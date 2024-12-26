from sqlmodel import SQLModel, create_engine
from sqlmodel import Session

# Define your database connection
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)

def init_db():
    # Create tables in the database
    SQLModel.metadata.create_all(engine)



def get_session():
    with Session(engine) as session:
        yield session
