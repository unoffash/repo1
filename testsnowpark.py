from snowflake.snowpark import Session
from snowflake.snowpark import types
from snowflake.snowpark import functions

# Set up Snowflake connection parameters
options = {
    "sfAccount": "rxrkbxe-dw20573",
    "sfDatabase": "HARNESSDB",
    "sfSchema": "HARNESSSCHEMA",
    "sfWarehouse": "COMPUTE_WH",
    "sfUser": "ASHP123",
    "sfPassword": "Idkth3sfpass@123"
}

# Start a Snowpark session
session = Session.builder().config(options).create()

# Read data from Snowflake table
source_table = session.read_table("SOURCE_HARNESS_TABLE")

# Show the DataFrame
source_table.show()

# Insert data into Snowflake table
target_table_name = "DESTINATION_HARNESS_TABLE"
source_table.write.format("snowflake").option("dbtable", target_table_name).save()

# Stop the Snowpark session
session.stop()
