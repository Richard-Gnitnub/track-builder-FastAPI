from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL)

# Create SessionLocal to handle sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    with SessionLocal() as session:
        yield session
