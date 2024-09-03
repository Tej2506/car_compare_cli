"""Initial migration

Revision ID: 8cff383cb1c5
Revises: 
Create Date: 2024-09-02 14:43:24.136459

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cff383cb1c5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manufacturers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('power', sa.String(), nullable=True),
    sa.Column('torque', sa.String(), nullable=True),
    sa.Column('engine', sa.String(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['manufacturers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('car_feature',
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('feature_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ),
    sa.ForeignKeyConstraint(['feature_id'], ['features.id'], ),
    sa.PrimaryKeyConstraint('car_id', 'feature_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car_feature')
    op.drop_table('cars')
    op.drop_table('manufacturers')
    op.drop_table('features')
    # ### end Alembic commands ###