from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:maazkhadim11@localhost:5000/productDBs"
engine = create_engine(db_url)
sessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)
