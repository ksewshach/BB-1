from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String




class UserDB(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True) # праймари ки - генерируется сам
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    # email: Mapped[str]
    password: Mapped[str] = mapped_column(String(255), nullable=False)


class UnitModel(Base):

    __tablename__ = "unit_table"

    id: Mapped[int] = mapped_column(primary_key=True) # праймари ки - генерируется сам
    title: Mapped[str]
    description: Mapped[str]
    # status: Mapped[bool] = mapped_column(default=False)

    # (...primary_key=True, index=True - индекс вроде для последующего поиска? Но времени и места тратится на него немало. Говорят.)


