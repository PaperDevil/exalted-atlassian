from datetime import datetime

import sqlalchemy
from sqlalchemy import Column, Table, ForeignKey, Integer, String, DateTime, Sequence, CheckConstraint, Text, Boolean


naming_convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(all_column_names)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

metadata = sqlalchemy.MetaData(naming_convention=naming_convention)

user_table = Table(
    'user', metadata,
    Column('id', Integer, Sequence('user_id_seq', start=1), primary_key=True),
    Column('created_at', DateTime, nullable=False, default=datetime.now),
    Column('edited_at', DateTime, nullable=False, default=datetime.now, onupdate=datetime.now),
    Column('telegram_id', String(24), nullable=False),
    Column('email', Text, CheckConstraint('char_length(email) >= 4 AND char_length(email) <= 100'), unique=True, nullable=True)
)
