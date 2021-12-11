"""structure

Revision ID: 2734ed11b75e
Revises:
Create Date: 2021-12-08 23:53:31.943338

"""
from alembic import op
import sqlalchemy as sa
from data.sql.uuid import UUID


# revision identifiers, used by Alembic.
revision = "2734ed11b75e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "storages",
        sa.Column("id", UUID(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("type", sa.String(length=50), nullable=True),
        sa.Column("key_secret_id", sa.String(length=200), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "etag",
            sa.String(length=50),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "albums",
        sa.Column("id", UUID(), nullable=False),
        sa.Column("storage_id", UUID(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=2000), nullable=True),
        sa.Column("public", sa.Boolean(), nullable=False),
        sa.Column("image_url", sa.String(length=2000), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "etag",
            sa.String(length=50),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["storage_id"], ["storages.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_albums_storage_id"), "albums", ["storage_id"], unique=False
    )
    op.create_table(
        "nodes",
        sa.Column("id", UUID(), nullable=False),
        sa.Column("album_id", UUID(), nullable=False),
        sa.Column("parent_id", UUID(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("type", sa.String(length=50), nullable=False),
        sa.Column("icon", sa.String(length=255), nullable=True),
        sa.Column("hidden", sa.Boolean(), nullable=False),
        sa.Column("folder", sa.Boolean(), nullable=False),
        sa.Column("file_id", sa.String(length=255), nullable=True),
        sa.Column("file_extension", sa.String(length=50), nullable=True),
        sa.Column("file_size", sa.Integer(), nullable=True),
        sa.Column("medium_image_name", sa.String(length=255), nullable=True),
        sa.Column("small_image_name", sa.String(length=255), nullable=True),
        sa.Column("image_width", sa.Integer(), nullable=True),
        sa.Column("image_height", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "etag",
            sa.String(length=50),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["album_id"], ["albums.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["parent_id"], ["nodes.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_nodes_album_id"), "nodes", ["album_id"], unique=False)
    op.create_index(op.f("ix_nodes_parent_id"), "nodes", ["parent_id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_nodes_parent_id"), table_name="nodes")
    op.drop_index(op.f("ix_nodes_album_id"), table_name="nodes")
    op.drop_table("nodes")
    op.drop_index(op.f("ix_albums_storage_id"), table_name="albums")
    op.drop_table("albums")
    op.drop_table("storages")
    # ### end Alembic commands ###
