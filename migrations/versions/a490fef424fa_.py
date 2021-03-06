"""empty message

Revision ID: a490fef424fa
Revises: 
Create Date: 2022-03-25 21:31:06.552717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a490fef424fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('trc_patient_id', sa.Integer(), nullable=False),
    sa.Column('uid_patient', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('trc_patient_id'),
    sa.UniqueConstraint('uid_patient')
    )
    op.create_table('experience',
    sa.Column('id_experience', sa.Integer(), nullable=False),
    sa.Column('trc_patient_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['trc_patient_id'], ['patient.trc_patient_id'], ),
    sa.PrimaryKeyConstraint('id_experience')
    )
    op.create_table('calory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_experience', sa.Integer(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('start_mesured_datetime', sa.DateTime(), nullable=True),
    sa.Column('end_mesured_datetime', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('end_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_experience'], ['experience.id_experience'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('step',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_experience', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('start_mesured_datetime', sa.DateTime(), nullable=True),
    sa.Column('end_mesured_datetime', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('end_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_experience'], ['experience.id_experience'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('step')
    op.drop_table('calory')
    op.drop_table('experience')
    op.drop_table('patient')
    # ### end Alembic commands ###
