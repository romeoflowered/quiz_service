from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from quiz_service.config import settings

engine = create_engine(settings.DATABASE_URL)

session_maker = sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
