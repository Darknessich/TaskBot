import enum
from typing import List
from datetime import datetime, timedelta
from sqlalchemy import ForeignKey, Table, Column, BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Status(enum.Enum):
    ACTIVE = "active"
    DONE = "done"
    DELETE = "delete"


class Reminder(Base):
    __tablename__ = "reminder"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger)
    description: Mapped[str]
    datetime: Mapped[datetime]
    period: Mapped[timedelta | None]
    status: Mapped[str]

    files: Mapped[List["File"]] = relationship(
        secondary="reminder_file",
        back_populates="reminders",
    )


reminder_file = Table(
    "reminder_file",
    Base.metadata,
    Column("reminder_id", ForeignKey("reminder.id"), primary_key=True),
    Column("file_id", ForeignKey("file.file_id"), primary_key=True),
)


class File(Base):
    __tablename__ = "file"

    file_id: Mapped[str] = mapped_column(primary_key=True)
    file_unique_id: Mapped[str]
    file_name: Mapped[str | None]

    reminders: Mapped[List["Reminder"]] = relationship(
        secondary="reminder_file",
        back_populates="files",
    )
