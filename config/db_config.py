# config/db_config.py

from mysql.connector import pooling

DB_CONFIG = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'sistema_experto',
}

db_connection_pool = pooling.MySQLConnectionPool(
    pool_name="pool",
    pool_size=5,
    **DB_CONFIG)
