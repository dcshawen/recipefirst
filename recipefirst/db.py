import sqlite3
from datetime import datetime

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        # Enable foreign key constraints
        g.db.execute('PRAGMA foreign_keys = ON')
    
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    
    try:
        # Create tables first
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
         
        db.commit()
        click.echo('Database schema created successfully.')
    except Exception as e:
        db.rollback()
        click.echo(f'Error creating database: {e}')
        raise

def patch_db():
    db = get_db()
    
    try:
        with current_app.open_resource('patch.sql') as f:
            db.executescript(f.read().decode('utf8'))
        db.commit()
        click.echo('Database patched successfully.')
    except Exception as e:
        db.rollback()
        click.echo(f'Error patching database: {e}')
        raise


@click.command('db-init')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

@click.command('db-patch')
def patch_db_command():
    """Patch the database."""
    patch_db()
    click.echo('Patch the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(patch_db_command)
    
# Data Operations
def getIngredients(limit = 0):
		"""Fetch all ingredients."""
		db = get_db()
		ingredients = db.execute('SELECT * FROM Ingredient').fetchall()
		return [dict(row) for row in ingredients]