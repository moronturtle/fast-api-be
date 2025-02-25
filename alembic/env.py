from sqlalchemy import engine_from_config, pool
from sqlalchemy.engine import create_engine
from alembic import context
import os

# Get DB URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)

def run_migrations_online():
    connectable = engine
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=None)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()