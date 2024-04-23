import os
import snowflake.connector

# Retrieve Snowflake connection details from environment variables
snowflake_account = 'ovtgwmt-ng13131'
snowflake_user = 'ASHWATHP'
snowflake_password = 'Idkth3flakepass@123'
snowflake_database = 'GITDB'
snowflake_schema = 'GITSCHEMA'

# SQL script to execute
sql_script = """
CREATE TABLE IF NOT EXISTS GITSCHEMA.GITTABLECICD (
    column1 VARCHAR(50),
    column2 INT
);
"""

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    database=snowflake_database,
    schema=snowflake_schema
)

# Create cursor
cur = conn.cursor()

# Execute SQL script
cur.execute(sql_script)

# Close cursor and connection
cur.close()
conn.close()
