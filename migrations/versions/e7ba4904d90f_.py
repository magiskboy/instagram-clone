"""empty message

Revision ID: e7ba4904d90f
Revises: 9fbaccee7c91
Create Date: 2020-08-17 09:43:31.852704

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e7ba4904d90f'
down_revision = '9fbaccee7c91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('n_followers', sa.Integer(), nullable=True))
    op.drop_column('users', 'n_follwers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('n_follwers', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('users', 'n_followers')
    # ### end Alembic commands ###
