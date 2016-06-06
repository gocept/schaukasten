"""Initialize DB

Revision ID: 4ab04e7a85ac
Revises: None
Create Date: 2016-06-02 15:37:02.919073

"""
from alembic import op
import sqlalchemy as sa
from schaukasten.db import GUID

# revision identifiers, used by Alembic.
revision = '4ab04e7a85ac'
down_revision = None


def upgrade():
    op.create_table(
        'contents',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('uuid', GUID(), nullable=False),
        sa.Column('raw_content', sa.LargeBinary()),
    )
    op.create_table(
        'files',
        sa.Column('id', GUID(), primary_key=True),
        sa.Column('filename', sa.String(255), nullable=False),
        sa.Column('mimetype', sa.String(100), nullable=False),
        sa.Column(
            'contents_id', sa.Integer(),
            sa.ForeignKey('contents.id', ondelete='cascade')),
    )


def downgrade():
    op.drop_table('files')
    op.drop_table('contents')
