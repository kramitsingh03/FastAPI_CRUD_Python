from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL, create_engine
from dotenv import load_dotenv
import os

# Load .env FIRST
load_dotenv()

# Create database URL
db_url = URL.create(
    "postgresql+psycopg2",
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)


# Create engine
engine = create_engine(db_url)

# Create session
session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)