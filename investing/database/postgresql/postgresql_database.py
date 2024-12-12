import logging
from ...config.config import DB_CONFIG
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_connection_string(DB_CONFIG):
    """Provides a database connection string from a valid DB_CONFIG."""
    if DB_CONFIG['type'] == 'postgresql':
        return f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    else:
        raise ValueError(f"Unsupported database type: {DB_CONFIG['type']}")

def create_tables(db_connection, db_schema = "./postgresql_schema.sql"):
    """Creates database tables."""
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(db_schema)
        conn.commit()
        logger.info("Database tables created successfully!")
    except psycopg2.Error as e:
        logger.error(f"Error creating database tables: {e}")
        raise

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()