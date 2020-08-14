"""empty message

Revision ID: 0c43fe3c3fa4
Revises: 33af94282f45
Create Date: 2020-08-13 09:01:39.159883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c43fe3c3fa4'
down_revision = '33af94282f45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fullname', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fullname')
    # ### end Alembic commands ###