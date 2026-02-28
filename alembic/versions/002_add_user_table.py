"""Add User table for authentication

Revision ID: 002_add_user_table
Revises: 001_initial
Create Date: 2026-02-28 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_add_user_table'
down_revision = '001_initial'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'User',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('hashed_password', sa.String(255), nullable=False),
        sa.Column('is_active', sa.Integer(), nullable=False, server_default='1'),
        sa.Column('is_superuser', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('user_id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email'),
    )
    op.create_index('ix_User_username', 'User', ['username'], unique=True)
    op.create_index('ix_User_email', 'User', ['email'], unique=True)


def downgrade() -> None:
    op.drop_index('ix_User_email', table_name='User')
    op.drop_index('ix_User_username', table_name='User')
    op.drop_table('User')
