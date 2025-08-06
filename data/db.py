import sqlite3
import os
from pathlib import Path

def init_db(db_name='recipefirst.db'):
    """
    Initialize a new SQLite database by executing the schema.sql file.
    
    Args:
        db_name (str): Name of the database file. Default is 'recipefirst.db'.
    
    Returns:
        str: Path to the created database file.
    """
    # Get paths
    current_dir = Path(__file__).parent
    root_dir = current_dir.parent
    instances_dir = current_dir / 'instances'
    os.makedirs(instances_dir, exist_ok=True)
    
    db_path = instances_dir / db_name
    schema_path = current_dir / 'schema.sql'
    
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found at {schema_path}")
    
    # Connect to the database
    with sqlite3.connect(db_path) as conn:
        # Read and execute the schema file
        with open(schema_path, 'r') as f:
            schema_sql = f.read()
        
        conn.executescript(schema_sql)
        
        print(f"Database initialized at {db_path}")
        return str(db_path)

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

def patch_db():
    """
    Apply patches to the database by executing the patch.sql file.
    
    Returns:
        str: Path to the patched database file.
    """
    # Get paths
    current_dir = Path(__file__).parent
    instances_dir = current_dir / 'instances'
    db_path = instances_dir / 'recipefirst.db'
    patch_path = current_dir / 'patch.sql'
    
    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found at {db_path}. Please run init_db() first.")
    
    if not patch_path.exists():
        raise FileNotFoundError(f"Patch file not found at {patch_path}")
    
    # Connect to the database
    with sqlite3.connect(db_path) as conn:
        # Read and execute the patch file
        with open(patch_path, 'r') as f:
            patch_sql = f.read()
        
        conn.executescript(patch_sql)
        
        print(f"Database patched successfully at {db_path}")
        return str(db_path)
