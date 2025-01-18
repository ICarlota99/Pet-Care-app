"""Add photo column to pets table

Revision ID: 8c868ccd6415
Revises: 63d7c63fec92
Create Date: 2025-01-17 19:40:25.595774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c868ccd6415'
down_revision = '63d7c63fec92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pet_profile_photo', sa.String(length=200), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('name',
               existing_type=sa.TEXT(),
               type_=sa.String(length=80),
               existing_nullable=False)
        batch_op.alter_column('sex',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('breed_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('sterilized',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('microchip_number',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('insurance_company',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('insurance_number',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.create_foreign_key(None, 'breeds', ['breed_id'], ['id'])
        batch_op.create_foreign_key(None, 'species', ['species_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('insurance_number',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('insurance_company',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('microchip_number',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('sterilized',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('breed_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('sex',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=80),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
        batch_op.drop_column('pet_profile_photo')

    # ### end Alembic commands ###
