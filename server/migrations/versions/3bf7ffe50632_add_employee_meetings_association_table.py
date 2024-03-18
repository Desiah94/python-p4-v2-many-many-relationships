"""add employee-meetings association table

Revision ID: 3bf7ffe50632
Revises: c9170e393ff6
Create Date: 2024-03-17 17:24:40.629665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bf7ffe50632'
down_revision = 'c9170e393ff6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees_meetings',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employees_meetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], name=op.f('fk_employees_meetings_meeting_id_meetings')),
    sa.PrimaryKeyConstraint('employee_id', 'meeting_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees_meetings')
    # ### end Alembic commands ###