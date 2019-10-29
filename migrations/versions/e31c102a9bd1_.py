"""empty message

Revision ID: e31c102a9bd1
Revises: 395df0a2f9f6
Create Date: 2017-12-09 12:29:30.316908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e31c102a9bd1'
down_revision = '395df0a2f9f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'master_password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('master_password_hash', sa.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###