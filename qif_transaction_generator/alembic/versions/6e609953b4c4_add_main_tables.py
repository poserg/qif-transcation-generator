"""Add main tables

Revision ID: 6e609953b4c4
Revises:
Create Date: 2019-01-07 19:23:37.990985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e609953b4c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('code', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('statuses',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('code', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('receipts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('fn', sa.String(), nullable=False),
                    sa.Column('fp', sa.String(), nullable=False),
                    sa.Column('fd', sa.String(), nullable=False),
                    sa.Column('purchase_date', sa.DateTime(), nullable=False),
                    sa.Column('total', sa.String(), nullable=False),
                    sa.Column('raw', sa.Text(), nullable=True),
                    sa.Column('ecash_total_sum', sa.Integer(), nullable=True),
                    sa.Column('cash_total_sum', sa.Integer(), nullable=True),
                    sa.Column('status_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('items',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('receipt_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('quantity', sa.Integer(), nullable=False),
                    sa.Column('sum', sa.Integer(), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['category_id'], ['categories.id'],
                                            ),
                    sa.ForeignKeyConstraint(['receipt_id'], ['receipts.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('dictionaries',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=False),
                    sa.Column('item_id', sa.Integer(), nullable=False),
                    sa.Column('phrase', sa.String(), nullable=False),
                    sa.Column('weight', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['category_id'], ['categories.id'],
                                            ),
                    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dictionaries')
    op.drop_table('items')
    op.drop_table('receipts')
    op.drop_table('statuses')
    op.drop_table('categories')
    # ### end Alembic commands ###
