from sqlalchemy import String, Text                         #String = short text, Text = long text
from sqlalchemy.orm import Mapped, mapped_column            #tools to describe a column
from .database import Base                                  #the parent class from database.py

class Record(Base):             #one Record = one row in the table
    __tablename__ = "records"   #the name of the table inside app.db

    id: Mapped[int] = mapped_column(primary_key=True)       #primary key column - unique number (auto-filled)
    title: Mapped[str] = mapped_column(String(255))         #title column - short text (max 255 characters)
    content: Mapped[str] = mapped_column(Text)              #long text, no real limit
    status: Mapped[str] = mapped_column(String(20), default="DRAFT")          #starts as DRAFT, if we don't specify a value, it will be DRAFT by default
    version: Mapped[int] = mapped_column(default=1)           #starts at 1, if we don't specify a value, it will be 1 by default
    created_by: Mapped[str] = mapped_column(String(100))            #who created the record, short text (max 100 characters)

    