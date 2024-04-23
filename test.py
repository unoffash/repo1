import os
import snowflake.connector

# Retrieve Snowflake connection details from environment variables
snowflake_account = os.getenv('secrets.SNOWFLAKE_ACCOUNT')
snowflake_user = os.getenv('secrets.SNOWFLAKE_USER')
snowflake_password = os.getenv('secrets.SNOWFLAKE_PASSWORD')
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
