"""user_settings

Revision ID: d4ac9ed5152d
Revises: 0af3ac006547
Create Date: 2021-09-18 20:53:12.160911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4ac9ed5152d'
down_revision = '0af3ac006547'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('edited_at', sa.DateTime(), nullable=False),
    sa.Column('notifications', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk__settings__user_id__user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__settings'))
    )


def downgrade():
    op.drop_table('settings')
