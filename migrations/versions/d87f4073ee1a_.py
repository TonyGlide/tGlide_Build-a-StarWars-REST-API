"""empty message

Revision ID: d87f4073ee1a
Revises: b549873eb945
Create Date: 2024-06-07 22:37:49.156327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd87f4073ee1a'
down_revision = 'b549873eb945'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('home_planet', sa.Integer(), nullable=True))
        batch_op.drop_constraint('person_planet_residing_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'planet', ['home_planet'], ['id'])
        batch_op.drop_column('homeworld')
        batch_op.drop_column('planet_residing')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_residing', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('homeworld', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('person_planet_residing_fkey', 'planet', ['planet_residing'], ['id'])
        batch_op.drop_column('home_planet')

    # ### end Alembic commands ###
