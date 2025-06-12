from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title}>"
