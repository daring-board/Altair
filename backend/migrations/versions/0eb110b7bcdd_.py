"""empty message

Revision ID: 0eb110b7bcdd
Revises: 
Create Date: 2019-03-31 18:58:02.375605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eb110b7bcdd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.Column('modified', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('concerts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.Column('modified', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_concerts_user_id'), 'concerts', ['user_id'], unique=False)
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('application', sa.DATETIME(), nullable=True),
    sa.Column('winning', sa.DATETIME(), nullable=True),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.Column('modified', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_members_name'), 'members', ['name'], unique=False)
    op.create_index(op.f('ix_members_user_id'), 'members', ['user_id'], unique=False)
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('concert_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('place', sa.String(length=255), nullable=False),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.Column('modified', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['concert_id'], ['concerts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_schedules_concert_id'), 'schedules', ['concert_id'], unique=False)
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('seate', sa.String(length=255), nullable=True),
    sa.Column('created', sa.DATETIME(), nullable=False),
    sa.Column('modified', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedules.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tickets_member_id'), 'tickets', ['member_id'], unique=False)
    op.create_index(op.f('ix_tickets_schedule_id'), 'tickets', ['schedule_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tickets_schedule_id'), table_name='tickets')
    op.drop_index(op.f('ix_tickets_member_id'), table_name='tickets')
    op.drop_table('tickets')
    op.drop_index(op.f('ix_schedules_concert_id'), table_name='schedules')
    op.drop_table('schedules')
    op.drop_index(op.f('ix_members_user_id'), table_name='members')
    op.drop_index(op.f('ix_members_name'), table_name='members')
    op.drop_table('members')
    op.drop_index(op.f('ix_concerts_user_id'), table_name='concerts')
    op.drop_table('concerts')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###