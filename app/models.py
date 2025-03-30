from database import Base
from sqlalchemy.orm import Mapped, mapped_column, Relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import List


class UserDB(Base):
    __tablename__ = "users"

    reg_number: Mapped[int] = mapped_column(primary_key=True, index=True) # праймари ки - генерируется сам
    id: Mapped[int] = mapped_column(Integer)
    username: Mapped[str] = mapped_column(String(25), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    

class ProjectDB(Base):
    __tablename__ = "projects"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    units: Mapped[List["UnitDB"]] = Relationship('UnitDB', back_populates='project')
    
    def __repr__(self):
        return f"<ProjectDB(title='{self.title}, id={self.id}')>"
    

class UnitDB(Base):
    __tablename__ = "units"

    id: Mapped[int] = mapped_column(primary_key=True, index=True) # а можно ли вообще без primaryKey? Или рили пусть это будет айдишник единицы.
    # owner_id: Mapped[int]
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey('projects.id'))
    
    project = Relationship('Project', back_populates='units')
    
    def __repr__(self):
        # def __repr__(self):
        return f"<UnitDB(title='{self.title}, id={self.id}')>"

