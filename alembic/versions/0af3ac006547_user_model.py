"""user model

Revision ID: 0af3ac006547
Revises: 
Create Date: 2021-09-12 19:22:44.541538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0af3ac006547'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('edited_at', sa.DateTime(), nullable=False),
    sa.Column('telegram_id', sa.String(length=24), nullable=False),
    sa.Column('email', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__user')),
    sa.UniqueConstraint('email', name=op.f('uq__user__email'))
    )


def downgrade():
    op.drop_table('user')
