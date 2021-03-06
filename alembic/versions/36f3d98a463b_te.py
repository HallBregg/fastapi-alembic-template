"""te

Revision ID: 36f3d98a463b
Revises: 8cec670f14c5
Create Date: 2020-09-02 17:08:26.905724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36f3d98a463b'
down_revision = '8cec670f14c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_description'), 'item', ['description'], unique=False)
    op.create_index(op.f('ix_item_id'), 'item', ['id'], unique=False)
    op.create_index(op.f('ix_item_title'), 'item', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_title'), table_name='item')
    op.drop_index(op.f('ix_item_id'), table_name='item')
    op.drop_index(op.f('ix_item_description'), table_name='item')
    op.drop_table('item')
    # ### end Alembic commands ###
