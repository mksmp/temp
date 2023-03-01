"""Add Images

Revision ID: 1a4fc0ce6eac
Revises: 1b05e51938c6
Create Date: 2022-06-12 21:53:34.279727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a4fc0ce6eac'
down_revision = '1b05e51938c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('filename', sa.String(length=100), nullable=False),
    sa.Column('mime_type', sa.String(length=100), nullable=False),
    sa.Column('md5_hash', sa.String(length=100), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('object_type', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_images_book_id_books')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_images')),
    sa.UniqueConstraint('md5_hash', name=op.f('uq_images_md5_hash'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    # ### end Alembic commands ###
