"""empty message

Revision ID: 3f46e691edc6
Revises: 4c7c79ed016d
Create Date: 2022-02-11 21:19:45.266140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f46e691edc6'
down_revision = '4c7c79ed016d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('wins', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('losses', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'losses')
    op.drop_column('user', 'wins')
    # ### end Alembic commands ###
