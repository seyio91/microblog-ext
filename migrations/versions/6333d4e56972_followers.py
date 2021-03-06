"""followers

Revision ID: 6333d4e56972
Revises: 7a8f52eb891b
Create Date: 2019-12-18 18:28:57.616964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6333d4e56972'
down_revision = '7a8f52eb891b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
