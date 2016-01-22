"""empty message

Revision ID: eaab6fc3ef59
Revises: 
Create Date: 2016-01-22 11:15:11.759745

"""

# revision identifiers, used by Alembic.
revision = 'eaab6fc3ef59'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('t1',
        sa.Column('c1', sa.Boolean(), nullable=True),
    )

    with op.batch_alter_table('t1', schema=None) as batch_op:
        batch_op.alter_column('c1', type_=sa.Integer(), existing_type=sa.Boolean())


def downgrade():
    pass
