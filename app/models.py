from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class UserDB(Base):

    __tablename__ = "users"

    reg_number: Mapped[int] = mapped_column(primary_key=True, index=True) # праймари ки - генерируется сам
    id: Mapped[int] = mapped_column(Integer)
    username: Mapped[str] = mapped_column(String(25), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)


class UnitDB(Base):

    __tablename__ = "unit_table"

    id: Mapped[int] = mapped_column(primary_key=True) # праймари ки - генерируется сам
    title: Mapped[str]
    description: Mapped[str]
    # status: Mapped[bool] = mapped_column(default=False)


