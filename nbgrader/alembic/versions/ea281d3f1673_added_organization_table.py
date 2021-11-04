"""Added organization table

Revision ID: ea281d3f1673
Revises: e43177bfe90b
Create Date: 2021-11-04 15:04:47.282526

"""
from uuid import uuid4

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ea281d3f1673'
down_revision = 'e43177bfe90b'
branch_labels = None
depends_on = None

def new_uuid() -> str:
    return uuid4().hex

def upgrade():
    op.create_table(
        'organization',
        sa.Column('id', sa.String(32), primary_key=True, default=new_uuid),
        sa.Column('name', sa.String(128), unique=True, nullable=False),
    )


def downgrade():
    op.drop_table('organization')
