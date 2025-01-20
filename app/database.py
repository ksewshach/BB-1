from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine(
    "sqlite:///db.sqlite",
    echo=True
)

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()