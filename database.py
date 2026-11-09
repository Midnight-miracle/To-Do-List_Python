import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

url = os.getenv("DATABASE_URL")
if not url:
    raise RuntimeError("DATABASE_URL is not set. Check your .env file.")
engine = create_engine(url)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)