"""empty message

Revision ID: d6bfdc8abadf
Revises: 
Create Date: 2017-10-21 18:36:38.644018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6bfdc8abadf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('genius_id', sa.Integer(), nullable=True),
    sa.Column('lyrics', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songsets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('key', sa.String(length=6), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('fname', sa.String(length=255), nullable=True),
    sa.Column('lname', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('is_auth', sa.Integer(), nullable=True),
    sa.Column('is_fitted', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs_join',
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('songset_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.ForeignKeyConstraint(['songset_id'], ['songsets.id'], ),
    sa.PrimaryKeyConstraint('song_id', 'songset_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs_join')
    op.drop_table('users')
    op.drop_table('songsets')
    op.drop_table('songs')
    # ### end Alembic commands ###