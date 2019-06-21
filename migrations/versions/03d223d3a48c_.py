"""empty message

Revision ID: 03d223d3a48c
Revises: 6d982c933936
Create Date: 2019-03-23 16:34:26.963387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03d223d3a48c'
down_revision = '6d982c933936'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_collect',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_collect')
    # ### end Alembic commands ###