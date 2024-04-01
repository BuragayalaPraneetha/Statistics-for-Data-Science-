
from trino import dbapi
 
# Connection parameters

host = 'trino.kashi-ka.ai'
port = 443  # Default Trino port for HTTPS
user = 'admin'
catalog = 'hive'
schema = 'kashika_schema'
http_scheme = 'https'  # Since it's HTTPS
 
try:

    # Establish connection

    conn = dbapi.connect(

        host=host,

        port=port,

        user=user,

        catalog=catalog,

        schema=schema,

        http_scheme=http_scheme

    )
 
    print("Successfully connected to Trino!")
 
    # Create cursor

    cursor = conn.cursor()
 
    # Execute query to show tables

    query = f'SHOW TABLES FROM {schema}'

    cursor.execute(query)
 
    # Fetch results

    tables = cursor.fetchall()
 
    # Print tables

    for table in tables:
        print(table[0]) 
except Exception as e:
    print(f"Failed to connect to Trino: {e}") 
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()