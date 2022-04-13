"""empty message

Revision ID: 8c605d0a9426
Revises: 
Create Date: 2022-04-13 18:23:11.144246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c605d0a9426'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coord', sa.String(length=32), nullable=True),
    sa.Column('area_name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=50000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_area_area_name'), 'area', ['area_name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_area_area_name'), table_name='area')
    op.drop_table('area')
    # ### end Alembic commands ###