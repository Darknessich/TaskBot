from datetime import date, datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models.reminders import Reminder, File, Status


class ReminderRepository:
    @staticmethod
    async def add_reminder(
        session: AsyncSession,
        chat_id: int,
        description: str,
        date: date,
        time: int,
        period: int,
        files: list[File],
    ):
        rdatetime = datetime(date.year, date.month, date.day, time // 60, time % 60)
        rperiod = ReminderRepository.__period_to_timedelta(period)

        reminder = Reminder(
            chat_id=chat_id,
            description=description,
            datetime=rdatetime,
            period=rperiod,
            status=Status.ACTIVE.value,
        )

        reminder.files = await ReminderRepository.__refresh_files(session, files)
        session.add(reminder)
        await session.commit()

    @staticmethod
    async def get_reminders_by_status(
        session: AsyncSession, chat_id: int, status: Status
    ):
        return list(
            await session.scalars(
                select(Reminder)
                .where(Reminder.chat_id == chat_id)
                .where(Reminder.status == status.value)
            )
        )

    @staticmethod
    async def get_reminder_by_id(session: AsyncSession, id: int):
        return await session.scalar(
            select(Reminder)
            .where(Reminder.id == id)
            .options(selectinload(Reminder.files))
        )

    @staticmethod
    async def update_reminder_status(session: AsyncSession, id: int, status: Status):
        reminder = await ReminderRepository.get_reminder_by_id(session, id)
        reminder.status = status.value
        await session.commit()

    @staticmethod
    async def update_reminder(
        session: AsyncSession,
        id: int,
        chat_id: int,
        description: str,
        date: date,
        time: int,
        period: int,
        files: list[File],
    ):
        rdatetime = datetime(date.year, date.month, date.day, time // 60, time % 60)
        rperiod = ReminderRepository.__period_to_timedelta(period)
        reminder = await ReminderRepository.get_reminder_by_id(session, id)
        reminder.chat_id = chat_id
        reminder.description = description
        reminder.datetime = rdatetime
        reminder.period = rperiod
        reminder.files = await ReminderRepository.__refresh_files(session, files)
        await session.commit()

    @staticmethod
    def __period_to_timedelta(period: int) -> timedelta | None:
        return (
            None
            if period == 0
            else timedelta(
                days=period // 1440, hours=(period // 60) % 24, minutes=period % 60
            )
        )

    @staticmethod
    async def __refresh_files(session: AsyncSession, files: list[File]) -> list[File]:
        file_ids = [file.file_id for file in files]
        base_files = await session.scalars(
            select(File).where(File.file_id.in_(file_ids))
        )

        base_ids = [file.file_id for file in base_files]
        new_files = [
            File(
                file_id=file.file_id,
                file_unique_id=file.file_unique_id,
                file_name=file.file_name,
            )
            for file in files
            if file.file_id not in base_ids
        ]

        session.add_all(new_files)
        return [*base_files, *new_files]
