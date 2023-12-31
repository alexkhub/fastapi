"""'initial'

Revision ID: b3fd6d7f9865
Revises: 
Create Date: 2023-12-30 14:40:55.026765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b3fd6d7f9865'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('category_name', sa.String(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('full_name', sa.String(length=50), nullable=False),
                    sa.Column('email', sa.String(length=70), nullable=False),
                    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('articles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user', sa.Integer(), nullable=True),
                    sa.Column('article_name', sa.String(length=70), nullable=False),
                    sa.Column('article_text', sa.Text(), nullable=True),
                    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('categories_articles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=True),
                    sa.Column('article', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['article'], ['articles.id'], ),
                    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('comments',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user', sa.Integer(), nullable=True),
                    sa.Column('article', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['article'], ['articles.id'], ),
                    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('liked_articles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user', sa.Integer(), nullable=True),
                    sa.Column('article', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['article'], ['articles.id'], ),
                    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('liked_articles')
    op.drop_table('comments')
    op.drop_table('categories_articles')
    op.drop_table('articles')
    op.drop_table('user')
    op.drop_table('categories')
    # ### end Alembic commands ###
