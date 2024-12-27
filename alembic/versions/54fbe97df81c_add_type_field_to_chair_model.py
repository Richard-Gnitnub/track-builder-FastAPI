from alembic import op
import sqlalchemy as sa
from sqlmodel import Field, SQLModel

# revision identifiers, used by Alembic.
revision = '54fbe97df81c'
down_revision = '5ab4ee8a296f'
branch_labels = None
depends_on = None

def upgrade():
    # Step 1: Add the 'type' column first
    with op.batch_alter_table("chair", schema=None) as batch_op:
        batch_op.add_column(sa.Column("type", sa.String(length=50), nullable=True))
    
    # Step 2: Add the 'track_id' column and its foreign key
    with op.batch_alter_table("chair", schema=None) as batch_op:
        batch_op.add_column(sa.Column("track_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "fk_chair_track_id", "track", ["track_id"], ["id"]
        )

def downgrade():
    # Step 2: Remove the foreign key and 'track_id' column
    with op.batch_alter_table("chair", schema=None) as batch_op:
        batch_op.drop_constraint("fk_chair_track_id", type_="foreignkey")
        batch_op.drop_column("track_id")
    
    # Step 1: Remove the 'type' column
    with op.batch_alter_table("chair", schema=None) as batch_op:
        batch_op.drop_column("type")
