import sqlite3
import os
import pathlib
import io

def init_db(db_name='recipefirst.db'):
    """
    Initialize a new SQLite database by executing the schema.sql file.
    
    Args:
        db_name (str): Name of the database file. Default is 'recipefirst.db'.
    
    Returns:
        str: Path to the created database file.
    """
    # Get the project root directory (parent of the data directory)
    root_dir = pathlib.Path(__file__).parent.parent
    
    # Create instances directory if it doesn't exist
    instances_dir = root_dir / 'data' / 'instances'
    os.makedirs(instances_dir, exist_ok=True)
    
    # Full path to the database file
    db_path = instances_dir / db_name
    
    # Full path to the schema file
    schema_path = root_dir / 'schema.sql'
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    
    try:
        # Read the schema file
        with open(schema_path, 'r') as f:
            schema_sql = f.read()
        
        # Execute the schema SQL
        conn.executescript(schema_sql)
        
        print(f"Database initialized at {db_path}")
        return str(db_path)
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
    finally:
        conn.close()

def getDBSchema():
    """
    Get the schema of the database.
    
    Returns:
        str: The SQL schema of the database.
    """
    # Get the project root directory (parent of the data directory)
    root_dir = pathlib.Path(__file__).parent.parent
    instances_dir = root_dir / 'data' / 'instances'
    db_path = instances_dir / 'recipefirst.db'
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query the sqlite_master table to get all table creation statements
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND sql IS NOT NULL")
    schema = cursor.fetchall()
    
    # Also get triggers, indices, and views
    cursor.execute("SELECT sql FROM sqlite_master WHERE type IN ('trigger', 'index', 'view') AND sql IS NOT NULL")
    schema.extend(cursor.fetchall())
    
    conn.close()
    return [item[0] for item in schema if item[0] is not None]