"""empty message

Revision ID: 6b2a79b77f99
Revises: 711568cf8813
Create Date: 2019-12-16 00:29:45.369092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b2a79b77f99'
down_revision = '711568cf8813'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transport',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('dep', sa.String(length=64), nullable=True),
    sa.Column('arr', sa.String(length=64), nullable=True),
    sa.Column('dep_time', sa.DateTime(), nullable=True),
    sa.Column('green_point', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transport')
    # ### end Alembic commands ###