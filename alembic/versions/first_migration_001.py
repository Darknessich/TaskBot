"""First migration

Revision ID: aa161ecd9ddc
Revises:
Create Date: 2024-10-12 06:57:17.421487

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aa161ecd9ddc"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "file",
        sa.Column("file_id", sa.String(), nullable=False),
        sa.Column("file_unique_id", sa.String(), nullable=False),
        sa.Column("file_name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("file_id"),
    )
    op.create_table(
        "reminder",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("chat_id", sa.BigInteger(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("datetime", sa.DateTime(), nullable=False),
        sa.Column("period", sa.Interval(), nullable=True),
        sa.Column("status", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "reminder_file",
        sa.Column("reminder_id", sa.Integer(), nullable=False),
        sa.Column("file_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["file_id"],
            ["file.file_id"],
        ),
        sa.ForeignKeyConstraint(
            ["reminder_id"],
            ["reminder.id"],
        ),
        sa.PrimaryKeyConstraint("reminder_id", "file_id"),
    )


def downgrade() -> None:
    op.drop_table("reminder_file")
    op.drop_table("reminder")
    op.drop_table("file")
